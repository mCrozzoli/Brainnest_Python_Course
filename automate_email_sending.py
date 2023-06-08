''' You work at a company that sends daily reports to clients via email. The goal of this project is to automate the process of sending these reports via email.

Here are the steps you can take to automate this process:

    Use the smtplib library to connect to the email server and send the emails.

    Use the email library to compose the email, including the recipient's email address, the subject, and the body of the email.

    Use the os library to access the report files that need to be sent.

    Use a for loop to iterate through the list of recipients and send the email and attachment.

    Use the schedule library to schedule the script to run daily at a specific time.

    You can also set up a log file to keep track of the emails that have been sent and any errors that may have occurred during the email sending process. '''

import smtplib
import os
import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

def connect_to_server(username, password, server_host='smtp-mail.outlook.com', port=587):
    # Connect to the mail server
    server = smtplib.SMTP(server_host, port)
    server.starttls()
    server.login(username, password)

    return server

def disconnect_from_server(server):
    # Disconnect from the server
    server.quit()
    
def send_email_with_attachements(server, subject, body, to, files, from_email):
    # Compose the email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    # Attach files
    for file in files:
        with open(file, 'rb') as f:
            #Creates a new MIMEBase object which represents a MIME entity. 
            #MIME is a way of identifying files on the Internet according to their nature and format. 
            #MIMEBase('application', 'octet-stream') creates an entity that contains some binary data.
            part = MIMEBase('application', 'octet-stream')
            #we pass the read data to the set_payload() method
            #which sets the payload (the data) of the MIME entity.
            part.set_payload(f.read())
            #This line encodes the payload into base64. 
            #The encoders.encode_base64(part) function is a specific MIME Content-Transfer-Encoding method 
            #that is used to safely encode binary data to ASCII text format.
            encoders.encode_base64(part)
            #This header is used to indicate that the part should be considered as an attachment, 
            #not part of the main body of the email, and also to suggest a filename for the attachment. 
            #The os.path.basename(filename) gets the filename without the preceding directory info.
            part.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
            #this line attaches the MIME entity (containing a base64 encoded attachment) to the message. 
            msg.attach(part)
    
    # Send the email
    server.send_message(msg)

def main_pipe(list_emails, server):
    subject = "Daily Report"
    body = "Please find attached the daily report (...)"
    
    #lists all the PDF files in the 'reports' sub-folder of the current working directory 
    files = [os.path.join('reports', filename) for filename in os.listdir('reports') if filename.endswith('.pdf')]

    for email in list_emails:
        send_email_with_attachements(server, subject=subject, body=body, to=email, files=files,
                                    from_email='sender_dk_@hotmail.com')

    print('\nFinished Sending emails')
    
    disconnect_from_server(server)

def main():
    # Replace with credentials
    username = 'username'
    password = 'password'
    server_host='smtp-mail.outlook.com'
    port=587

    server = connect_to_server(username=username, password=password, server_host=server_host, port=port)

    # Replace these with your recipients' emails
    list_emails = ['juan@gmail.com', 'juan@outlook.com']

    # Schedule the job every day at ...
    schedule.every().day.at("15:18").do(main_pipe, list_emails, server)

    while True:
        schedule.run_pending()

main()

'''
# Code Report

This script is used for the purpose of automating sending daily reports via email, with the reports being PDF attachments.

## Imports

The script uses several Python modules to achieve its purpose:

- `smtplib`: This module is used for sending emails using the Simple Mail Transfer Protocol (SMTP).
- `os`: This module provides a way of using operating system dependent functionality.
- `schedule`: This module is an in-process scheduler for periodic jobs using the builder pattern for configuration. It allows you to schedule jobs to be run periodically.
- `time`: This module provides various time-related functions.
- `email.mime.multipart`, `email.mime.base`, `email.mime.text`, `email.encoders`: These are used for constructing MIME messages, including attachments.

## Functions

The script includes several functions:

- `connect_to_server(username, password, server_host='smtp-mail.outlook.com', port=587)`: This function connects to the specified SMTP server using the provided username and password, and returns the server connection object.
- `disconnect_from_server(server)`: This function disconnects from the specified SMTP server.
- `send_email_with_attachments(server, subject, body, to, files, from_email)`: This function constructs an email with the specified subject and body, adds any specified files as attachments, and sends the email to the specified recipient.
- `main_pipe(list_emails, server)`: This function prepares the email body and subject, locates all the PDF files in the 'reports' directory, sends emails with the reports attached to each of the recipients in `list_emails`, and then disconnects from the SMTP server.
- `main()`: This function connects to the SMTP server, schedules the `main_pipe()` function to run at a specified time every day, and then enters a loop where it repeatedly runs any pending scheduled jobs.

## Code Flow

When the `main()` function is called:

1. It connects to the SMTP server using provided credentials (`username`, `password`, `server_host`, `port`).

2. A list of recipients' emails is defined in `list_emails`.

3. The script schedules the `main_pipe` function to run daily at 15:18. The `main_pipe` function will:
   - Gather all the .pdf files from the 'reports' folder.
   - For each email in `list_emails`, it sends an email with the PDF files attached.
   - Once all emails are sent, it disconnects from the server.

4. After scheduling, the script enters a loop where it keeps checking for any pending scheduled jobs and runs them when their scheduled time arrives.

## Implementation

Before running the script, you need to replace placeholder variables with your own actual values:

- Replace `'username'` and `'password'` in the `main()` function with your actual email username and password.
- Replace the emails in `list_emails` with your actual recipients' emails.
- You might also need to adjust the scheduled time in the `schedule.every().day.at("15:18")` call to match your requirements.

To run the script, you simply run it like any Python script, for example using a command like `python script_name.py` in a command prompt. Ensure that the Python environment where you run the script has the `smtplib`, `os`, `schedule`, `time`, and `email` modules installed. Also make sure you have a 'reports' directory with PDF files in the same directory as the script.

## Library description:

1. **`smtplib`:** This library is used for sending emails using the Simple Mail Transfer Protocol (SMTP). `smtplib.SMTP` is a class used to encapsulate an SMTP connection. It takes an SMTP server and the server’s port as arguments. To secure the SMTP connection, `server.starttls()` is used. To login into the server, `server.login(username, password)` is used. And to send an email, `server.send_message(msg)` is used.

2. **`os`:** This library provides a portable way of using operating system-dependent functionality. It's used here to get the filenames of the reports to be attached, using `os.listdir('reports')` to get a list of all files in the 'reports' directory and `os.path.join('reports', filename)` to get the full path to each file. `os.path.basename(file)` is also used to get the base name of a file without the directory path.

3. **`schedule`:** This library provides an easy-to-use scheduler for running jobs at specified times. `schedule.every().day.at("15:18").do(main_pipe, list_emails, server)` is used to schedule `main_pipe` to run every day at 15:18. `schedule.run_pending()` is then used in a loop to keep checking and running any pending scheduled jobs.

4. **`time`:** This library provides various time-related functions. Although this module has been imported in the script, it is not used in the current version of the script.

5. **`email.mime.multipart`:** This module provides the `MIMEMultipart` class, which is used to create MIME messages that can contain multiple parts. `MIMEMultipart()` is used here to create a new email, with `msg.attach()` used to add parts (the email body and attachments) to the email.

6. **`email.mime.base`:** This module provides the `MIMEBase` class, which is a base class for all the MIME-specific subclasses of `Message`. It's used here to create the email attachments with `MIMEBase('application', 'octet-stream')`.

7. **`email.mime.text`:** This module provides the `MIMEText` class, which is used to create MIME objects of major type text. `MIMEText(body, 'plain')` is used here to create the email body.

8. **`email.encoders`:** This module provides the `encode_base64` function, which encodes the payload into base64 form, where the payload is the data that you want to send. `encoders.encode_base64(part)` is used here to encode the attachments before adding them to the email. This is needed because email can't handle raw binary data.
'''