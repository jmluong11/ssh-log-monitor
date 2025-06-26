# SSH Log Monitor with Email Alerts

A Python script that monitors `/var/log/auth.log` for failed SSH login attempts. When suspicious IPs exceed a defined threshold, it sends an email alert.

## Features
- Detects failed SSH login attempts
- Flags IPs with repeated failed logins
- Sends alert emails automatically
- Cron-compatible for automated scheduling

## Setup

1. Clone this repo:
   ```bash
   git clone https://github.com/yourname/ssh-log-monitor.git
   cd ssh-log-monitor