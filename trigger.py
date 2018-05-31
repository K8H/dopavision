#!/usr/bin/env python3

import smtplib
from email.mime.text import MIMEText

class Trigger(object):

    def __init__(self):
        self.dopavisionEmail = 'k8hofmann@gmail.com'
        self.email = 'k8hofmann@gmail.com'

    def sendEmail(self, dbCursor):
        textfile = 'email'
        
        #fp = open(textfile, 'rb')
        msg = MIMEText('You should go out for a bit')
        #fp.close()

        msg['Subject'] = 'Dopavision alert'
        msg['From'] = self.dopavisionEmail
        msg['To'] = self.email
        
        s = smtplib.SMTP('localhost', 1025)
        s.sendmail(self.dopavisionEmail, [self.email], msg.as_string())
        s.quit()
