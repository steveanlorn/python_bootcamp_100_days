import pandas
import datetime as dt
import os
import random
import smtplib

EMAIL = ""
PASSWORD = ""
SENDER_NAME = "Steve"

email_connection = smtplib.SMTP("smtp.gmail.com")
email_connection.starttls()
email_connection.login(user=EMAIL, password=PASSWORD)

bdf = pandas.read_csv("birthdays.csv")

now = dt.datetime.now()
birth_day_today_df = bdf[
    (bdf.year == now.year) &
    (bdf.month == now.month) &
    (bdf.day == now.day)
]

templates = []
for tmp in os.listdir("./letter_templates"):
    with open(f"./letter_templates/{tmp}") as template_file:
        content = template_file.read()
        content = content.replace("[SENDER_NAME]", SENDER_NAME)
        templates.append(content)

for friend in birth_day_today_df.itertuples():
    message_template = random.choice(templates)
    email_body = message_template.replace("[NAME]", friend.name)
    print(f"Sending to {friend.name}, {friend.email}")
    email_connection.sendmail(
        from_addr=EMAIL,
        to_addrs=friend.email,
        msg=f"Subject:Happy Birthday!\n\n{email_body}")

email_connection.close()
