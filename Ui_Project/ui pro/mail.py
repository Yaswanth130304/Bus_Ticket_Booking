from email.message import EmailMessage
import imghdr
import smtplib

app_pass = "fyeaftawgwbadjyd"
host_user="tt282258@gmail.com"
clef = "gayithrikandikunta@gmial.com"

smtp = smtplib.SMTP_SSL('smtp.gmail.com',465)
smtp.login(host_user,app_pass)

msg = EmailMessage()

with open('./images/a.png','rb') as f: 
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name



msg['Subject'] = "Welcome to AKIO Treavels"
msg['From'] = host_user
msg['To'] = clef
msg.set_content("Hello Dude. Our Team members will soon contact you for further approach.")
msg.add_attachment(file_data,maintype="image", subtype=file_type,filename=file_name)



smtp.send_message(msg)