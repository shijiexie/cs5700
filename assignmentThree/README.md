
# SMTP Mail Client

## Overview
This program is a Python-based SMTP client that connects to an SMTP server (like smtp.gmail.com) to send emails. It demonstrates the implementation of the SMTP protocol without using high-level libraries such as `smtplib`.

## Setup and Running Instructions
1. **Prerequisites:** Ensure Python is installed on your system.
2. **Configuration:**
   - Edit the script to include your email address and password at the designated placeholders.
   - If using Gmail, set up an [Application Specific Password](https://support.google.com/accounts/answer/185833) for authentication.
   - Modify the SMTP server and port as needed (default is set for Gmail).
3. **Running the Program:** Execute the script by running `python a3.py` in the terminal.

## Input Parameters
- Sender's email address and password.
- Recipient's email address.
- SMTP server address and port.
- Email content.

## Expected Output
- The program will display the sequence of SMTP commands sent and the responses received from the server.
- A successful email delivery will end with a '250 OK' response from the server.

## Note
- The script does not implement high-security measures and is intended for educational purposes.
