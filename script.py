import requests
from bs4 import BeautifulSoup
import smtplib
import time
# https://myaccount.google.com/lesssecureapps?pli=1
gmailFrom = ""
gmailTo = ""
password = ""

URL = "http://tfg.esup.upf.edu/tfg/pfc_consultar_pfcs.jsp?estudi=ei"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'}

def checkPrice():
  page = requests.get(URL, headers=headers)

  soup = BeautifulSoup(page.content, 'html.parser')

  title = soup.find(class_="taula").get_text()
  tfgs = soup.find_all('tr')
  info = tfgs[2].get_text().replace(u'\xa0', u' ')
  text = "Link:" + URL + "Info:" + info
  if len(tfgs) > 153:
    subject = "New TFG!"
    body = text
    msg = f"Subject: {subject}\n\n{body}"
    sendMail(msg)

def sendMail(msg):
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()

  server.login(gmailFrom, password)

  server.sendmail(
    gmailFrom,
    gmailTo,
    msg
  )

  print('Email has been sent')
  server.quit()

while(True):
  checkPrice()
  time.sleep(60 * 60 * 24)