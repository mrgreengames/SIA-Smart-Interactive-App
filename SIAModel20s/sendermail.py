# Test code for Sending mail
# DO NOT PUT THIS IN GIT HUB
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = ''  # Email of Sender
email_send = ''  # Email of Recipient
subject = "Python!"

msg = MIMEMultipart()
msg["From"] = email_user
msg["To"] = email_send
msg["Subject"] = subject
body = 'Hello, sending this email from Python'
msg.attach(MIMEText(body, 'plain'))

filename = 'document.txt'
attachment = open(filename, 'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= " + filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_user, 'PASSWORD')

server.sendmail(email_user, email_send, text)
server.quit()
