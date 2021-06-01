import smtplib
from email.message import EmailMessage

def send_mail(user_id,user_password,reciever_id,subject,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login(user_id,user_password)
    email = EmailMessage()
    email['From'] = user_id
    email['To'] = reciever_id
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)

#make this dynamic and pass the value in the function thats it!

send_mail('pass values here')