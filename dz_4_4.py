from datetime import date
from requests import get, utils

response = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp"))

def currency_rate(codes):
    content = response.split('Valute ID=')
    d, m, y = map(int, content[0].split('"')[-4].split('.'))

    for val in content:
        if codes.upper() in val:
            print(date(year=y, month=m, day=d), end=':  ')
            return float(val.replace('/', "").split('<Value>')[-2].replace(',', '.'))

if __name__ == "__main__":
    print(currency_rate('uSD'))
    print(currency_rate('EUR'))



from dz_4_4 import utils

print(utils.currency_rate(HUF))







