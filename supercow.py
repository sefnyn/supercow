# Monitor Samvera/Hydra/Sufia web app

import http.client
import datetime
import smtplib
from email.message import EmailMessage

SERVER = 'collections.durham.ac.uk'
OUTGOING = 'smtphost.dur.ac.uk'
COWFILE = 'cow'
page = 'web_page.html'
fh = open(page, 'w')

conn = http.client.HTTPSConnection(SERVER)
conn.request('GET', "/")
r1 = conn.getresponse()
if (r1.status != 200):
    #send e-mail alert
    print(datetime.datetime.now(), "HTTP", r1.status, "Super Cow could not retrieve web page")
    msg = EmailMessage()
    with open(COWFILE) as fp:
        msg.set_content(fp.read())
    msg['Subject'] = '*** Super Cow could not retrieve web page from ' + SERVER
    msg['From'] = 'SuperCow@bovines.org'
    msg['To']   = 'pzvx49@durham.ac.uk'
    s = smtplib.SMTP(OUTGOING)
    s.send_message(msg)
    s.quit()
else:
    data1 = r1.read()
    fh.write(str(data1))
    print(datetime.datetime.now(), "HTTP", r1.status, str(len(data1)), "bytes retrieved")
    fh.close()
conn.close()
