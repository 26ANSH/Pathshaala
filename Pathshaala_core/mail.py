import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

BODY = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body{
            padding: 4vh; 
        }
    </style>
    <title>This is Pathshaala</title>
</head>
<body>
<h1>Welcome to Pathshaala</h1>
</body>
</html>
'''
me = "pathshalla_1234@outlook.com"
text = "hello, maanas"
s = smtplib.SMTP('smtp.office365.com',587)

s.ehlo()
s.starttls()
s.login(me, 'Path1234')

email = '19bcs4047@cuchd.in'

message = MIMEMultipart()

message['From'] = me
message['To'] = email
message['Subject'] = 'Hello, How are you ?'

part = MIMEText(BODY, 'html')
message.attach(part)

for _ in range(10):
    s.sendmail(me, email, message.as_string())

print("Mail send to >> ",email)

s.quit()





