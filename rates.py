import requests
from bs4 import BeautifulSoup
import pandas as pd

# #----------------KAPITAL BANK -------------------#
KAPITALBANK_URL = "https://kapitalbank.uz/uz/welcome.php"

response_kapitalbank = requests.get(KAPITALBANK_URL)

kapitalbank_website_html = response_kapitalbank.text

soup_kapitalbank = BeautifulSoup(kapitalbank_website_html, "html.parser")

currency_tags =soup_kapitalbank.select(selector=".item .item-picture")
rate_tag_buy =soup_kapitalbank.select(selector=".item-rate-buy .item-value")
rate_tag_sell =soup_kapitalbank.select(selector=".item-rate-sale .item-value")

rate_list_buy = [(rate.getText()) for rate in rate_tag_buy]
rate_list_sell = [(rate.getText()) for rate in rate_tag_sell]
curr_list = [(currency.getText()) for currency in currency_tags]


# rate_list_buy = ' '.join([(rate.getText()) for rate in rate_tag_buy])
#
# rate_list_sell = ' '.join([(rate.getText()) for rate in rate_tag_sell])
#
# curr_list = ' '.join([(currency.getText()) for currency in currency_tags])

print("------ KAPITALBANK --------")
print(curr_list[:4])
print(rate_list_buy)
print(rate_list_sell)

new_data_kapitalbank = {
    "Currency": curr_list[:4],
    "Buy_Rate": rate_list_buy,
    "Sell-Rate": rate_list_sell,
}

df_kapitalbank = pd.DataFrame(new_data_kapitalbank)

df_kapitalbank.to_csv("Currency.csv", mode="w", index=False, header=False)


#----------------NBU -------------------#

NBU_URL = "https://nbu.uz/en/exchange-rates/"

response_nbu = requests.get(NBU_URL)

nbu_website_html = response_nbu.text

soup_nbu = BeautifulSoup(nbu_website_html, "html.parser")
# print(asakabank_website_html)
nbu_currency_tags =soup_nbu.select(selector=".kursdata table tr td")


# print(nbu_currency_tags[:20])

for_slicing = nbu_currency_tags[:20]

# print(for_slicing[slice(2,3)] + for_slicing[slice(5, 6)] + for_slicing[slice(11, 12)] + for_slicing[slice(8,9)])
nbu_buy = for_slicing[slice(1,2)] + for_slicing[slice(4,5)] + for_slicing[slice(10,11)] + for_slicing[slice(7,8)]
nbu_sell = for_slicing[slice(2,3)] + for_slicing[slice(5, 6)] + for_slicing[slice(11, 12)] + for_slicing[slice(8,9)]


# asakabank_curr_list = [(currency.getText()) for currency in asakabank_currency_tags]
nbu_rate_list_buy = [(rate.getText()) for rate in nbu_buy]
nbu_rate_list_sell = [(rate.getText()) for rate in nbu_sell]

print(nbu_rate_list_buy)
print(nbu_rate_list_sell)

new_data_nbu = {
    "Currency": ["USD", "EUR", "GBP", "RUB"],
    "Buy_Rate": nbu_rate_list_buy,
    "Sell-Rate": nbu_rate_list_sell,
}

df_nbu = pd.DataFrame(new_data_nbu)

df_nbu.to_csv("Currency.csv", mode="a", index=False, header=False)

#----------------NBU -------------------#

INFIN_URL = "https://www.infinbank.com/en/"

response_infin = requests.get(INFIN_URL)

infin_website_html = response_infin.text

soup_infin = BeautifulSoup(infin_website_html, "html.parser")
# print(soup_infin)
infin_currency_tags =soup_infin.select(selector=".ticker__desc_sub")


# print(infin_currency_tags)


infin_curr_list = [(currency.getText()) for currency in infin_currency_tags]
print(infin_curr_list)
# nbu_rate_list_buy = [(rate.getText()) for rate in nbu_buy]
# nbu_rate_list_sell = [(rate.getText()) for rate in nbu_sell]
#
# print(nbu_rate_list_buy)
# print(nbu_rate_list_sell)
#
new_data_infin_ = {
    "Currency": ["USD", "EUR", "GBP", "RUB"],
    "Buy_Rate": nbu_rate_list_buy,

}

df_infin_ = pd.DataFrame(new_data_infin_)

df_infin_.to_csv("Currency.csv", mode="a", index=False, header=False)