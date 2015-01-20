#!/usr/bin/python
'''
Created on Nov 5, 2014

@author: tony
'''
import ReportGenerator
import MailSender

subject = ReportGenerator.generateReportTitle()
emailBody = ReportGenerator.generateReportBody()

mailServer = "mail-relay.autodesk.com"
sender = "rendering.monitor@autodesk.com"
#receiver = ["wei.feng@autodesk.com"]
receiver = ["home.floorplanner.shanghai@autodesk.com","3dmon@juran.cn"]

MailSender.send_mail(mailServer, sender, receiver, subject, emailBody)

if __name__ == '__main__':
    pass