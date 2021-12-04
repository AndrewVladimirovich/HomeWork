from requests import get, utils
from decimal import Decimal
from re import findall

response = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp"))

def currency_rate(codes):
    content = response.split('Valute ID=')
    for val  in content:
        if codes.upper() in val:
            print(codes.upper(), end=' ')
            return float(val.replace('/', "").split('<Value>')[-2].replace(',', '.'))
print(currency_rate('uSD'))
print(currency_rate('EUR'))
