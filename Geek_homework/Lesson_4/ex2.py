from requests import get, utils


response = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp"))

def currency_rates(code):
    valute = response.split("<Valute ID=")
    for i in valute:
        if code.upper() in i:
            return float(i.replace("/", "").split("<Value>")[1].replace(",", "."))

if __name__ == "__main__":
    print(currency_rates("EUR"))
    print(currency_rates("USD"))
    print(currency_rates("GBP"))
    print(currency_rates("Bitcoin"))
    print("it is not the main executable")