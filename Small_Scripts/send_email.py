import mail
html_file = "C:\\Users\\fengw\\Desktop\\2.html"
text = mail.file_reader(html_file)
#mail_server = {"name":"mail-relay.autodesk.com"}
mail_server = "mail-relay.autodesk.com"
receiver = ["wei.feng@autodesk.com"]
attachment = ["C:\\Users\\fengw\\Desktop\\mail.py","C:\\Users\\fengw\\Desktop\\send_email.py"]
mail.send_mail(mail_server, "wei.feng@autodesk.com", receiver, "This is a test email",text,attachment)
