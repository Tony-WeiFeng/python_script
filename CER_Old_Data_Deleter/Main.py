'''
Created on Dec 10, 2013

@author: fengw
'''
import datetime
import Deleter
import mail

# Get the folder name 
d = datetime.date.today()

year = d.year - 3
month = d.month

folderName = "%d-%d" % ( month, year )
fullPath = "X:\\" + folderName

# remove the *.zip and *dump files
delete = Deleter.Deleter()
freeSize = str( delete.deleter( fullPath ) )
    


# set parameters of email content

text = 'Hi Team,<br><br>\n\
According to our CER new retention policy, we just keep the CER payloads for 36 months. So the *.zip and *.dump files of <font color="red"><b>' + folderName + '</b></font> have been deleted from CER file server.<br>\n\
There are about <font color="red"><b>' + freeSize + ' GB</b></font> space has been released in total at this time.<br><br>\n\
Thanks,<br>\n\
CER Admin'
mail_server = "mail-relay.autodesk.com"
#receiver = ["wei.feng@autodesk.com"]
receiver = ["cer-admin-support@autodesk.com"]
attachment = []

# send email
#mail.send_mail( mail_server, "wei.feng@autodesk.com", receiver, "This is a test email ", text, attachment )
mail.send_mail( mail_server, "cer-admin-support@autodesk.com", receiver, "CER payloads purge notification", text, attachment )
