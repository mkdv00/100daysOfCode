import smtplib
import random
import datetime as dt

email = "bootcamp1223@gmail.com"
password = "..."

with open("quotes.txt") as data_file:
    quotes = data_file.readlines()

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs="bootcamp1223@yahoo.com",
            msg=f"Subject: Congratulations\n\n {random.choice(quotes)}"
        )
