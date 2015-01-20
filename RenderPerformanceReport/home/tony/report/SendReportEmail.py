'''
Created on Oct 6, 2014

@author: tony
'''
import GenerateReport
from home.tony.email import MailSender
gr = GenerateReport.ReportGenerator()
gr.generateEmailConnect()

mailServer = "mail-relay.autodesk.com"
sender = "wei.feng@autodesk.com"
#receiver = ["wei.feng@autodesk.com"]
receiver = ["wei.feng@autodesk.com","william.jin@autodesk.com"]
subject = gr.title
msg = gr.messageString

MailSender.send_mail(mailServer, sender, receiver, subject, msg)

if __name__ == '__main__':
    pass