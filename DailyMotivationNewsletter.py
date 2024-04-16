import os, smtplib
import datetime as dt, random
import Credentials, Counter
from email.mime.image import MIMEImage
from email.header import Header
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart

my_email, password, to_email, prev_day = Credentials.my_email, Credentials.password, Credentials.to_email, Counter.prev_day

now = dt.datetime.now()
weekday = now.weekday()

if weekday != prev_day:
    with open("Counter.py", "w") as f:
        f.write(f"prev_day = {weekday}")
    f.close()

    ImgNum = random.randint(1, 22)
    ImgFileName = f"./Images/{ImgNum}.jpg"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)

        with open(ImgFileName, 'rb') as f:
            img_data = f.read()

        msg = MIMEMultipart()
        msg['Subject'] = 'Daily Motivation'
        msg['From'] = formataddr((str(Header('PythonMail', 'utf-8')), my_email))
        msg['To'] = to_email

        image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
        msg.attach(image)
        connection.sendmail(my_email, to_email, msg.as_string())
        connection.quit()
