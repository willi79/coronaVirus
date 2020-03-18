import smtplib
import time
i=0
while(i<5):
    server = smtplib.SMTP('smtp.mailgun.org', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('postmaster@sandbox9a81f6ab2bed4f17801a176da0ad5b42.mailgun.org', 'b64eb177bc7caa81f841ef64fa43b99b-1df6ec32-d0c0f265')
    subject = 'Email Test'
    body = "Test"
    msg = "Subject: None"
    server.sendmail('postmaster@sandbox9a81f6ab2bed4f17801a176da0ad5b42.mailgun.org','willigeraldy@gmail.com',msg)
    server.quit()
    time.sleep(100)