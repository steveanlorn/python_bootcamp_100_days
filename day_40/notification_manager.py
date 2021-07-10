import smtplib

MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = ""
MY_PASSWORD = ""


def send_emails(users, message):

    with open("email_template.txt", mode="r") as file:
        template = file.read()

    with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        for user in users:
            print(f"sending email for {user['email']}")
            message_body = template.replace("[first_name]", user["firstName"])
            message_body = message_body.replace("[tickets]", message)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=user["email"],
                msg=f"Subject:Penerbangan Murah Untuk {user['firstName']}!\n\n{message_body}".encode('utf-8')
            )
