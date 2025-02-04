import requests
import re
import os
import logging

# Setup logging configuration
logging.basicConfig(filename="malicious_ips.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# List of trusted IPs that should never be blocked
trusted_ips = ["192.168.1.1", "192.168.0.100"]

# Function to log the action of blocking an IP
def log_blocked_ip(ip, reason):
    logging.info(f"Blocked IP: {ip} due to: {reason}")
    print(f"Blocked IP: {ip} due to: {reason}")

# Function to check if the IP is malicious based on multiple criteria
def is_malicious(ip):
    if ip in trusted_ips:
        print(f"IP {ip} is trusted. No action needed.")
        return False  # Trusted IP, don't block

    url = f"https://api.abuseipdb.com/api/v2/check"
    headers = {
        'Key': 'Your Api Key Here',
        'Accept': 'application/json'
    }
    params = {
        'ipAddress': ip
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()

        abuse_confidence_score = data['data']['abuseConfidenceScore']
        num_reports = data['data']['totalReports']
        num_distinct_users = data['data']['numDistinctUsers']
        is_tor = data['data']['isTor']

        # Combine the criteria to detect malicious IP
        if abuse_confidence_score > 90 or num_reports > 1 or num_distinct_users > 2 or is_tor:
            return True
        else:
            return False
    else:
        print(f"Error checking IP {ip}: {response.status_code}")
        return False

# Function to extract valid IPs from log file
def extract_ips(log_file):
    with open(log_file, "r") as file:
        logs = file.readlines()

    ips = set()
    # Regular expression for matching valid IP addresses
    ip_pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"

    for line in logs:
        # Search for IPs in the log line
        found_ips = re.findall(ip_pattern, line)
        for ip in found_ips:
            ips.add(ip)

    return ips

# Example function to block malicious IPs using netsh (Windows firewall)
def block_ip(ip):
    # Command to block IP using Windows netsh firewall
    command = f'netsh advfirewall firewall add rule name="Block {ip}" dir=in action=block protocol=TCP remoteip={ip}'
    os.system(command)  # This will execute the command to block the IP
    log_blocked_ip(ip, "Abuse confidence score > 90 or other malicious indicators")

# Example usage
log_file = r"Path to your log file"  # Path to your log file
extracted_ips = extract_ips(log_file)

print("Extracted IPs:", extracted_ips)

for ip in extracted_ips:
    print(f"Checking IP: {ip}")
    if is_malicious(ip):
        print(f"IP {ip} is malicious. Taking action!")
        block_ip(ip)  # Block the IP
    else:
        print(f"IP {ip} is safe, no action needed.")
