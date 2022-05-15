import requests
from bs4 import BeautifulSoup
import smtplib
from time import sleep

email = ""
password = "" 
mails= ["",""]
sleep(3600)
urlw = "https://market.samm.com/raspberry-pi-zero-w-en"
urlwh = "https://market.samm.com/raspberry-pi-zero-wh-en"
versionW = requests.get(urlw)
versionWh = requests.get(urlwh)
Soupw = BeautifulSoup(versionW.content,"html5lib")
Soupwh = BeautifulSoup(versionWh.content,"html5lib")
w = Soupw.find("div",{"class":"fl col-12 mb-50 stock-durum2"}).text
wh = Soupwh.find("div",{"class":"fl col-12 mb-50 stock-durum2"}).text
print (wh)
print(mails[0])
if "Out of stock" not in w:
    with smtplib.SMTP("smtp.gmail.com",587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(email, password)
        subject = "text."
        body = "text."
        msg = f"Subject: {subject}\n\n{body}"
        smtp.sendmail(email,mails[0],msg)

if "Out of stock" not in wh:
    with smtplib.SMTP("smtp.gmail.com",587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(email, password)
        subject = "etx"
        body = "text."
        msg = f"Subject: {subject}\n\n{body}"
        smtp.sendmail(email,mails[0],msg)
