import smtplib
from email.message import EmailMessage

user_id = input("enter your mail id:")
user_password = input("enter the password:")
reciever = input("enter reciever address:")
subject = input("enter subject:")
content = input("enter content:")

def send_mail(user_id,user_password,reciever_id,subject,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    #This class manages a connection to an SMTP or ESMTP server.
    #calling smtplib and creating SMTP server
    server.starttls()
    #Puts the connection to the SMTP server into TLS mode
    #in simple words Authentication
    
    # Make sure to give app access in your Google account
    
    server.login(user_id,user_password)
   
    #entering credentials
    email = EmailMessage()
    email['From'] = user_id
    email['To'] = reciever_id
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)



send_mail(user_id,user_password,reciever,subject,content)