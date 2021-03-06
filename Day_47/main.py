from bs4 import BeautifulSoup
import smtplib
import requests
import lxml

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 " \
             "Safari/537.36 OPR/73.0.3856.400"
accept_language = "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
link = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"

headers = {
    "User-Agent": user_agent,
    "Accept-Language": accept_language
}

response = requests.get(
    url=link,
    headers=headers
)

soup = BeautifulSoup(response.text, "lxml")

price = soup.find(name="span", id="priceblock_ourprice").getText()
float_price = float(price.split("$")[1])

if float_price <= 120:
    product_name = soup.find(name="span", class_="product-title-word-break").getText().strip()

    message = f"{product_name} is now {price}\n{link}"

    email = "bootcamp1223@gmail.com"
    password = "Qwerty_123"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs="bootcamp1223@yahoo.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}"
        )
