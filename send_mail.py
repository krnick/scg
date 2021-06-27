import smtplib
from email.mime.text import MIMEText
from CSVReader import CSVReader

from config import ACCOUNT, PASSWORD
from helper import get_mail_content
from time import sleep

# Your Account
gmail_user = ACCOUNT
gmail_password = PASSWORD


def send_mail(name, mail, title):
    msg = MIMEText(get_mail_content(name, title), "html", "utf-8")
    msg['Subject'] = "PyCon Taiwan 2021: Call for Proposals is now Open"
    msg['From'] = "Shirley Lin"
    msg['To'] = mail
    msg['Cc'] = "program@pycon.tw"

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.send_message(msg)
    server.quit()


if __name__ == '__main__':

    accpeted_list = CSVReader("list.csv")

    for name, mail in accpeted_list.get_rows():
        if name == "Name":
            continue

        send_mail(name, mail)
        print(f"Send to {name}, with {mail}")

        sleep(2)
