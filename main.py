import csv
import datetime as dt
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random, smtplib
from userpass import UserPass

emailPass = []
with open("/Users/yamlak/Desktop/emailpass.txt") as userData:
    for line in userData:
        emailPass.append(line)

USER = UserPass(emailPass[0], emailPass[1])
SERVER = 'smtp.gmail.com'
PORT = 587 # Port 587 is used for email submission, supports SSL and TSL use
today = dt.datetime.now()
# MIME: multipurpose internet email extentions

def send_email(subject, body, sender, recepient):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recepient
    msg.attach(MIMEText('\n'+ body, 'plain'))

    with smtplib.SMTP(SERVER, PORT) as s:
        s.ehlo() # identifies yourself to ESMTP server using EHLO (extended hello). "Hello, I'm an STMP client and want to use the extended command set"
        s.starttls() # encrypts email message, TLS means transport layer security
        s.login(USER.email, USER._UserPass__password) # logs into email, use of name mangled variables because password is a private variable
        s.sendmail(from_addr=USER.email, to_addrs="yamlakdshim@gmail.com", msg=msg.as_string())
    print('Sending Message...')
    print('Message Sent!')

def mondayMotivation():
    if today.weekday()==0:
        with open('quotes.txt') as quotes:
            quotesList = []
            for line in quotes:
                quotesList.append(line)
        send_email(subject = 'Monday Monday Monday! Let`s get pumped!', body = random.choice(quotesList), sender = USER.email, recepient= input('Sending To: '))
    else:
        print('Today is not Monday thankfully')

def bdayWish():
    file_path = f"/Users/yamlak/Documents/automatedEmail/letters/letter_{random.randint(1,3)}.txt"
    with open('birthdays.csv') as bdays:
        reader = csv.reader(bdays)
        for name, email, year, month, day in reader:
            if str(today.month) == month and str(today.day) == day:
                print(f'It\'s {name}\'s birthday today!')
                with open(file_path) as letters:
                    content = letters.read()
                    modified_content = content.replace("[NAME]", name)
                    send_email(subject= f'Happy Birthday {name}!', body = modified_content , sender=USER.email, recepient=email)
            else:
                if name != 'name':
                    print(f'Not {name}\'s  birthday today')


# send_email('test', 'hello', 'testyams1@gmail.com', 'yamlakdshim@gmail.com') Test line
mondayMotivation()
bdayWish()


