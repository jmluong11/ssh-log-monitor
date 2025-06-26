# SSH Log Monitor with Email Alerts

A Python-based security monitoring tool that continuously parses SSH authentication logs to detect and alert on potential brute-force login attempts.

## Project Overview
This project automates the detection of suspicious SSH login failures by parsing log files (/var/log/auth.log or any specified log), identifying IP addresses with repeated failed login attempts beyond a configurable threshold, and sending real-time email notifications to security personnel.
<img src="https://i.imgur.com/6B0idf6.png" height="80%" width="100%"/>
It is designed to run as a cron job for continuous monitoring, helping system administrators proactively respond to unauthorized access attempts.



## Key Features
- __Log Parsing__: Utilizes Python’s regular expressions to efficiently scan SSH authentication logs for failed login attempts.
- __Threshold-Based Alerting__: Flags IP addresses exceeding a configurable failure count, minimizing noise and false positives.
- __Email Notifications__: Sends detailed alerts via SMTP, enabling timely incident response.
- __Cron Job Integration__: Easily scheduled on Linux systems for automated, hands-off security monitoring.

## Skills & Technologies Demonstrated
- __Python Scripting__: Proficient use of file I/O, regex, and email libraries (smtplib, email.message) to create a functional monitoring tool.
- __Linux System Knowledge__: Understanding of Linux authentication logs and common security attack patterns (e.g., SSH brute-force).
- __Automation & Scheduling__: Leveraged cron jobs to automate script execution and ensure continuous protection.
- __Security Awareness__: Implemented threshold-based detection to reduce false positives and integrated secure email sending practices.
- __Version Control__: Managed project versioning using Git and hosted the repository on GitHub for collaboration and showcase.



## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/yourname/ssh-log-monitor.git
   cd ssh-log-monitor
2. Configure settings:
   Edit config.py to specify your log file path, email server details, threshold values, and alert recipients.
3. Run the script manually or schedule it via cron:
   ```bash
   python ssh_log_monitor.py

## Potential Improvements
- Add support for other log sources or formats.
- Integrate with messaging platforms like Slack for alerting.
- Implement IP blocking or firewall integration for automatic mitigation.
- Extend parsing to detect other types of suspicious activity.
