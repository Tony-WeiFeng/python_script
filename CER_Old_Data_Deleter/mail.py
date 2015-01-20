'''
Created on Dec 10, 2013

@author: fengw
'''
# File name mail.py
 
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

# python 2.3.*: email.Utils email.Encoders
from email.utils import COMMASPACE, formatdate
from email import encoders

import os


#server['name'], server['user'], server['passwd']
def send_mail( server, fro, to, subject, text, files = [] ): 
    assert type( server ) == str 
    assert type( to ) == list 
    assert type( files ) == list 

    msg = MIMEMultipart() 
    msg['From'] = fro 
    msg['Subject'] = subject 
    msg['To'] = COMMASPACE.join( to ) #COMMASPACE==', ' 
    msg['Date'] = formatdate( localtime = True ) 
    msg.attach( MIMEText( text, 'html' ) ) 

    for file in files: 
        part = MIMEBase( 'application', 'octet-stream' ) #'octet-stream': binary data 
        part.set_payload( open( file, 'rb' ).read() ) 
        encoders.encode_base64( part ) 
        part.add_header( 'Content-Disposition', 'attachment; filename="%s"' % os.path.basename( file ) ) 
        msg.attach( part ) 

    import smtplib 
    smtp = smtplib.SMTP( server ) 
    #smtp.login(server['user'], server['passwd']) 
    smtp.sendmail( fro, to, msg.as_string() ) 
    smtp.close()

#mail_server = {"name":"mail-relay.autodesk.com"}
#receiver = ["wei.feng@autodesk.com"]
#send_mail (mail_server, "wei.feng@autodesk.com", receiver, "This is a test email","this is a test mail")

def file_reader( filename ):
    file_object = open( filename )
    try:
        content = file_object.read()
    except IOError, e:
        print "File open error:", e
    finally:
        file_object.close()
    return content

