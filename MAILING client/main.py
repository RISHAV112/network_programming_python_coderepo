from email import encoders
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server=smtplib.SMTP('smtp.gmail.com',465)
server.ehlo()
with open('password.txt','r') as f:
    password=f.read()
server.login('sender_mail_id','password')
msg=MIMEMultipart()
msg['from']='gmail'
msg['to']='receiver_mail_id'
msg['Subject']='this is a test message'
with open('message.txt','r') as f:
    message=f.read()

msg.attach(MIMEText(message,'plain'))
filename='image_file'
attachment=open(filename,'rb')
p=MIMEBase('application','octet-stream')
p.set_payload(attachment.read())
encoders.encode_base64(p)
p.add_header('Content-Disposition',f'attachment;filename={filename}')
msg.attach(p)
text=msg.as_string()
server.sendmail('sender_mail_id','receiver_mail_id',text)


