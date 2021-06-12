import random
import datetime as dt
import smtplib

EMAIL = ""
PASSWORD = ""


def get_quote():
    with open("quotes.txt") as quote_file:
        quote_list = quote_file.readlines()
        return random.choice(quote_list)


now = dt.datetime.now()
if now.weekday() == 5:
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)

        quote = get_quote()
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Motivation Quote Of The Day\n\n{quote}")
