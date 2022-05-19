import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
import smtplib

#Loading username and password for account from a separate secrets file
f = open('config.secret',)
data = json.load(f)


def sendEmail(emailToaddr, subjectLine, messageBody):
    '''
    Given a receiver email address, subject line, and message body; this
    function will send an email to the address provided.
    '''
 
    #setup the MIME
    message = MIMEMultipart()
    #Decoding secrets as they are stored as base64 
    message['From'] = str(base64.standard_b64decode(data["user_name"])).strip("b'")
    message['To'] = str(emailToaddr)
    message['Subject'] = str(subjectLine)

    #The body of the message
    message.attach(MIMEText(messageBody, 'plain'))

    #Create STMP session for sending email
    session = smtplib.SMTP('smtp.gmail.com', 587) #Using gmail with SMTP port
    session.starttls() #enable secure connection
    session.login(str(base64.standard_b64decode(data["user_name"])).strip("b'"), str(base64.standard_b64decode(data["user_pass"])).strip("b'"))
    text = message.as_string()
    session.sendmail(str(base64.standard_b64decode(data["user_name"])).strip("b'"), emailToaddr, text)
    session.quit()
    print("Mail Sent")