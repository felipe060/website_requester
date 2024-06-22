import time
import requests
import smtplib
import email.message
from dotenv import find_dotenv, load_dotenv
from os import getenv, environ

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)


def send_email_200():
    email_body = 'website status --> Response [200]'
    print('email_body --> ', email_body)
    print('email_body type -->', type(email_body))

    msg = email.message.Message()
    msg['Subject'] = 'Python flask login vercel'
    msg['From'] = 'your_email@email.com'
    msg['To'] = 'your_email@email.com'
    password = environ.get('PASSWORD_GOOGLE')
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_body)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('email sent, I hope')


def send_email_error():
    email_body = 'website status --> deu errado alguma coisa aí, meu nobre'
    print('email_body --> ', email_body)
    print('email_body type -->', type(email_body))

    msg = email.message.Message()
    msg['Subject'] = 'Python flask login vercel'
    msg['From'] = 'your_email@email.com'
    msg['To'] = 'your_email@email.com'
    password = environ.get('PASSWORD_GOOGLE')
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_body)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('email sent, I hope')


while True:
    requisicao = requests.get('https://flasklogin.vercel.app')
    requisicao = str(requisicao)
    print(requisicao)

    if requisicao == '<Response [200]>':
        send_email_200(     #u must close this parentesis, then the code will work, i hope
        time.sleep(20)
    else:
        send_email_error()
        time.sleep(20)
