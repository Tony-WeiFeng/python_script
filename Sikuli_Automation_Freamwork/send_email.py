# File name: send_email.py

import mail

# set parameters of email content
html_file = "C:\\Users\\Administrator\\Desktop\\Automation_Freamwork\\result.html"
text = mail.file_reader(html_file)
mail_server = "mail-relay.autodesk.com"
receiver = ["wei.feng@autodesk.com"]
attachment = ["C:\\Users\\Administrator\\Desktop\\Automation_Freamwork\\result.html","C:\\Users\\Administrator\\Desktop\\Automation_Freamwork\\send_email.py"]

# send email
mail.send_mail(mail_server, "wei.feng@autodesk.com", receiver, "This is a test email",text,attachment)
