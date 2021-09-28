from email.mime import text
import requests

from bs4 import BeautifulSoup

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import datetime

now = datetime.datetime.now();

content = ''; #using the content variable to store the data that we will scrap, in the start that data will be null

def extract_news(url):
    print("Starting to extract the news")
    cnt = ''
    cnt = cnt + ("<b>HN Top Stories: </b>\n" + "<br>" + "-"*50+"<br>")
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,"html.parser")
    for i,tag in enumerate(soup.find_all('td',attrs={"class":"title","valign":""})):
        cnt = cnt + ((str(i+1) + " :: " + tag.text + "\n" + "<br>") if tag.text != "More" else '')
    
    return cnt

cnt = extract_news('https://news.ycombinator.com/')
content = content + cnt
content = content + ("<br>------<br>")
content = content + ("<br><br> End of the title of the news")


print("Creating the email")


SERVER = "smtp.gmail.com" #the smtp server
PORT = 587
FROM = ""
TO = ""
PASS = ""



msg = MIMEMultipart()

msg['Subject'] = 'Top News Stories HN [Email-Automatizado]' + ' ' + str(now.day) + '-' + str(now.month) + '-' + str(now.year)

#Here our focous is on creating a dynamic email, so it won't be filtered as a spam and it will improve the organization of your email

msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))

print('trying to initialize the server')

server = smtplib.SMTP(SERVER,PORT)

server.set_debuglevel(1)
server.ehlo() #initializing the server
server.starttls() #starting the tls connection
server.login(FROM,PASS) # loggin with the login passed and the password
server.sendmail(FROM,TO,msg.as_string())

print('Email enviado')

server.quit()