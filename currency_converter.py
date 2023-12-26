import requests

API_KEY = "fca_live_OjM6mCOXLgikz2Ru758RAhottPo45lsDkdu7tO8t"
BASE = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY", "KRW","PHP","INR","IDR"]

CURRENCIES_list={"USD":"US DOLLAR", "CAD":"CANADIAN DOLLAR", "EUR":"EUROPIAN DOLLAR", "AUD":"AUSTRALIAN DOLLAR", "CNY":"Chinese Yuan", "KRW":"South Korean Won","PHP":"Philippine Peso","INR":"Indian Rupee","IDR":"Indonesian Rupiah"}

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except:
        print("Invalid ")

# while True:
#
#     inp = input("Enter the base currency to be converted : ").upper()
#     inp_amount = int(input("Enter the amount that is to be converted: "))
#
#     data_req = convert_currency(inp)
#
#     for key, value in data_req.items():
#         if key == inp:
#             pass
#         else:
#             print(f"{CURRENCIES_list[key]}: {float(value)*inp_amount}")
#     print()