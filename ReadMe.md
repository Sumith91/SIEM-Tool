SIEM Tool - Simple Security Event Monitoring System




📌 Overview
SIEM Tool is a lightweight Security Information and Event Management (SIEM) system that passively analyzes Windows log files, detects malicious IP addresses, and blocks threats using Windows Firewall.

🚀 Features
✔ Extracts and analyzes IP addresses from firewall logs
✔ Checks IP reputation using AbuseIPDB API
✔ Blocks malicious IPs automatically using Windows Firewall (netsh)
✔ Generates detailed reports of blocked threats
✔ Fully automated, requiring minimal manual intervention

🛠️ Technologies Used
Python (Requests, Regex, OS module)
AbuseIPDB API (for checking IP reputation)
Windows Firewall (netsh) (for blocking threats)
Log Analysis (Extracts suspicious IPs from logs)
💾 Installation & Usage
🔧 Prerequisites
Python 3.8+ installed
API key from AbuseIPDB
Run the script as Administrator to block IPs
🚀 Installation Steps
1️⃣ Clone the repository

bash
Copy
Edit
git clone https://github.com/your-username/SIEM-Tool.git
cd SIEM-Tool
2️⃣ Install dependencies

bash
Copy
Edit
pip install requests
3️⃣ Run the script in Administrator Mode

bash
Copy
Edit
python siem_tool.py
4️⃣ Check blocked IPs in Windows Firewall

bash
Copy
Edit
netsh advfirewall firewall show rule name=all
📜 License
This project is licensed under the MIT License – you are free to use, modify, and distribute it.

🤝 Contributing
We welcome contributions! To contribute:

Fork the repository
Create a new branch (git checkout -b feature-branch)
Commit your changes (git commit -m "Add new feature")
Push to your fork (git push origin feature-branch)
Create a Pull Request
📧 Contact & Support
If you face any issues, feel free to open an Issue or contact us at sumithsourav@gmail.com