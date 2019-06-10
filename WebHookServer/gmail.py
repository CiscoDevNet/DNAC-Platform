from __future__ import print_function
import smtplib
import sys
import os
# hide the spark token
sys.path.append(os.path.join(os.path.dirname(__file__), "config"))
from gmail_config import gmail_user, gmail_password

def send_mail(header, message):
    sent_from = "dnac@cisco.com"
    to = [gmail_user]
    subject = header
    body = message

    email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print ('Email sent!')
    except:
        print ('Something went wrong...')
