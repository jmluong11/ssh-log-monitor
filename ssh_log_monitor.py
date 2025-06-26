#!/usr/bin/env python3

import re
from email.message import EmailMessage
import smtplib
from config import LOG_FILE, THRESHOLD, SMTP_SERVER, SMTP_PORT, EMAIL_USER, EMAIL_PASS, EMAIL_TO

def parse_log():
    fail_pattern = re.compile(r"Failed password for.*from (\d+\.\d+\.\d+\.\d+)")
    ip_failures = {}

    try:
        with open(LOG_FILE, "r") as file:
            for line in file:
                match = fail_pattern.search(line)
                if match:
                    ip = match.group(1)
                    ip_failures[ip] = ip_failures.get(ip, 0) + 1
    except FileNotFoundError:
        print(f"Log file not found: {LOG_FILE}")
        return []

    suspicious_ips = [f"{ip} ({count} attempts)" for ip, count in ip_failures.items() if count >= THRESHOLD]
    return suspicious_ips

def send_email_alert(ip_list):
    msg = EmailMessage()
    msg['Subject'] = "🚨 SSH Alert: Failed Login Attempts Detected"
    msg['From'] = EMAIL_USER
    msg['To'] = EMAIL_TO
    msg.set_content("Suspicious IPs with multiple failed SSH login attempts:\n\n" + "\n".join(ip_list))

    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.login(EMAIL_USER, EMAIL_PASS)
            smtp.send_message(msg)
        print("Email sent successfully.")
    except Exception as e:
        print("Error sending email:", e)

def main():
    suspicious_ips = parse_log()
    if suspicious_ips:
        send_email_alert(suspicious_ips)
    else:
        print("No suspicious activity detected.")

if __name__ == "__main__":
    main()