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
    <title>Pathshaala - Updates</title>
</head>
<body style="padding: 4vh">
<h1>{}</h1>
<h4>{}</h4>
<h5><a href="{}">{}</a></h5>
<p>{}</p>
</body>
</html>
'''
# me = "pathshalla_1234@outlook.com"
me = "ansh.vidyabhanu@studentambassadors.com"

def Send_Email(to, subject, head, sub_head, link, link_text, extra=''):
    s = smtplib.SMTP('smtp.office365.com',587)
    s.ehlo()
    s.starttls()
    s.login(me, 'MayWeMeetAgain_26')
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = to
    msg.attach(MIMEText(BODY.format(head, sub_head, link, link_text, extra), 'html'))
    s.send_message(msg)
    del msg
    s.quit()


send = ['19bcs4074@cuchd.in','19bcs4076@cuchd.in','19bcs4085@cuchd.in','19bcs4047@cuchd.in']
for mail in send:
    print("sending to",mail)
    Send_Email(mail, 'checking', 'This is Pathshaala', 'Thank you for registering with us', 'https://pathshaala.azurewebsites.net', 'Click here to login', 'Thank you for registering with us.')