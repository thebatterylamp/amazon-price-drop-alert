from bs4 import BeautifulSoup
import requests
import string
import smtplib

MY_EMAIL = "YOUR_EMAIL_HERE"
MY_PASSWORD = "YOUR_APP_PASS_HERE"

headers = {
    "Accept-Language": "en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

# product_name = "Kindle"
product_url = "https://www.amazon.in/All-new-Kindle-2022-release-high-resolution/dp/B09SWSPYHW/ref=sr_1_2?crid=1QE4DSOX3JEVG&keywords=kindle&qid=1697828591&sprefix=kindle%2Caps%2C229&sr=8-2"
respone = requests.get(product_url, headers=headers)
html_data = respone.text
soup = BeautifulSoup(html_data, "html.parser")

price_tag = soup.find(name="span", class_="a-price-whole")
product_name = soup.find(name="span", id="productTitle")

str_price = price_tag.getText()
str_name = product_name.getText()


def remove_punctuation(input_string):
    translator = str.maketrans("", "", string.punctuation)
    result = input_string.translate(translator)
    return result


output = remove_punctuation(str_price)
price = int(output)

if price < 10000:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="thejellofish@icloud.com",
                            msg=f"Subject:Price Dropped!\n\nDear Asif,\nThere is a price drop. Please check {product_url}.")

