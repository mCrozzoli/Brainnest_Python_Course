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