# from abc import ABC, abstractmethod
# import datetime as dt
# import csv
# import datetime as dt
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import random, smtplib
# from userpass import UserPass


# SERVER = 'smtp.gmail.com'
# PORT = 587 # Port 587 is used for email submission, supports SSL and TSL use
# USER = UserPass(input("Enter your email: "), input('Enter your password: '))

# class AbstractBaseEmail(ABC):

#     # MIME: multipurpose internet email extentions

#     user = UserPass(email = "testyams1@gmail.com", password = 'ulgegtorjailvwum')
#     def __init__(self,subject, body, sender, recepients):
#         self.subject = subject
#         self.body = body
#         self.sender = sender
#         self.recepients = recepients
    
#     @abstractmethod
#     def send_email(self, subject, body, sender, recepients):
#         pass


# class mondayEmail(AbstractBaseEmail):
#     def send_email(self):
#         msg = MIMEMultipart("alternative")
#         msg["Subject"] = self.subject
#         msg["From"] = self.sender
#         msg["To"] = self.recepients
#         msg.attach(MIMEText('\n'+ self.body, 'plain'))
#         with smtplib.SMTP(SERVER, PORT) as s:
#             s.ehlo() # identifies yourself to ESMTP server using EHLO (extended hello). "Hello, I'm an STMP client and want to use the extended command set"
#             s.starttls() # encrypts email message, TLS means transport layer security
#             s.login(USER.email, USER._UserPass__password) # logs into email, use of name mangled variables because password is a private variable
#             s.sendmail(from_addr=USER.email, to_addrs="yamlakdshim@gmail.com", msg=msg.as_string())
#         with open('quotes.txt') as quotes:
#             quotesList = []
#             for line in quotes:
#                 quotesList.append(line)
#         self.send_email(subject = input('Subject: '), body = random.choice(quotesList), sender = user.email, recepients= input('Sending To: '))
#     print('Sending Message...')
#     print('Message Sent!')

