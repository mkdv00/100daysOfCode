# import smtplib
# 
# my_email = "bootcamp1223@gmail.com"
# password = "..."
# 
# # Добавляем smtp адресс нашей почты и создаем соединение
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     # Шифруем сообщение
#     connection.starttls()
#     # Авторизовываемся на почту
#     connection.login(user=my_email, password=password)
#     # Отправляем сообщение
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="bootcamp1223@yahoo.com",
#         msg="Subject: Hello world\n\nThis is the body of my email."
#     )


import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()

if year == 2021:
    print("Wear a face maks")

print(day_of_week)

date_of_birth = dt.datetime(year=2000, month=1, day=10)
print(date_of_birth)