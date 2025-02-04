# SIEM-Tool
SIEM Tool is a lightweight Security Information and Event Management (SIEM) system that passively analyzes Windows log files, detects malicious IP addresses, and automatically blocks threats using Windows Firewall. This tool helps in identifying potential cyber threats based on real-time log analysis.
1. Download the Project Files
Go to the GitHub repository link shared with you (e.g., https://github.com/your-username/SIEM-Tool).
Click on the "Code" button (green) and select "Download ZIP".
Extract the ZIP file to a folder on your computer.
2. Install Python (if not already installed)
Download Python from python.org.
Install Python and make sure to check the box that says "Add Python to PATH".
Verify the installation by opening Command Prompt and typing:
bash
Copy
Edit
python --version
3. Install Required Python Libraries
Open Command Prompt (as Administrator for firewall changes).
Navigate to the project folder:
bash
Copy
Edit
cd path\to\SIEM-Tool
Install dependencies using:
bash
Copy
Edit
pip install -r requirements.txt
4. Configure the Project
Open config.json file in a text editor (e.g., Notepad).
Replace "your-abuseipdb-api-key" with your actual API key from AbuseIPDB.
Update the log file path to point to your actual log file:
json
Copy
Edit
{
    "api_key": "your-abuseipdb-api-key",
    "log_file_path": "C:\\path\\to\\your\\logfile.log",
    "abuse_threshold": 90,
    "report_threshold": 2
}
5. Run the SIEM Tool
Ensure Command Prompt is running as Administrator:
Right-click Command Prompt and choose "Run as administrator".
Run the tool:
bash
Copy
Edit
python siem_tool.py
The tool will:
Extract IPs from the log file.
Check if any IPs are malicious using AbuseIPDB.
Block malicious IPs using Windows Firewall.
6. Check Blocked IPs in Windows Firewall (Optional)
To view the blocked IPs:
bash
Copy
Edit
netsh advfirewall firewall show rule name=all
7. Troubleshooting Common Issues
Error: 'requests' module not found:
Run pip install requests to install the missing library.
No malicious IPs found:
Ensure your log file has valid IP addresses.
Check that the API key is correctly set in config.json.
Firewall rules not applying:
Ensure Command Prompt is running as Administrator.
Check Windows Firewall settings for active rules.
8. Viewing Logs (Optional)
Check the logs/ folder for detailed logs of blocked IPs.
