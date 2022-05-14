import re

from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import shapiro
# Skrypt sprawdzający czy rozkład ceny mieszkań w Warszawie jest rozkładem normalnym
# H0: Ceny mieszkań w Warszawie układają się w rozkład normalny.
# H1: Ceny mieszkań w Warszawie nie układają się w rozkład normalny.
URL = 'https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/warszawa'
rows =[]
prices_out = []
licznosci = []
def parse_values(number):
    print(f'Pracuje nad strona numer {number}.')
    page = get(f'{URL}&?page={number}')
    bs = BeautifulSoup(page.content, 'html.parser')

    for offer in bs.find_all('li', class_='css-p74l73 es62z2j17'):

        price = (offer.find('div', class_='css-itig98 eclomwz1').get_text().strip())
        split_price = price.split("zł" or "€", 1)



        value_of_price = split_price[0]

        if value_of_price.startswith("Zapytaj o cenę",):
            value = value_of_price
        else:
            value_of_price1 = value_of_price



        prices = float(value_of_price1.replace('\xa0',"").replace(",",'.'))

        area = offer.find('div', class_='css-itig98 eclomwz1').get_text().strip()
        split_area = area.replace("pokoje", "   ")
        split_area = split_area.replace("pokoj", "   ")
        split_area = split_area.replace("pokój", "   ")
        split_area = split_area.replace("pokoi", "   ")
        split_area = split_area.replace("zł", "   ")
        split_area = split_area.replace(" €", "   ")
        last_chars = split_area[-8:]
        last_chars1 = last_chars.replace(" m²", "")

        value_of_area = float(last_chars1)
        #print(prices)
        rows.append([prices,value_of_area])
        prices_out.append(prices)
for page in range(1,10):
    parse_values(page)
df = pd.DataFrame(rows,columns=(['Cena','Powierzchnia']))
#print("wartosc minimalna i maksymalna",min(prices_out),max(prices_out))
bins = [0,100000,200000,300000,400000,500000,600000,700000,800000,900000,1000000,1100000,4000000]
cat = pd.cut(x=prices_out,bins=bins,include_lowest=True)

ax = cat.value_counts().plot.bar(rot=90, color="black", figsize=(30,20))
test = shapiro(prices_out)
print(test)
plt.show()
# wniosek: p-value < 0.05 co pozwala stwierdzic, że rozkład cen mieszkan na 10
# stronach serwisu otodom nie jest rozkładem normalnym.Hipoteza1 jest prawdziwa.

