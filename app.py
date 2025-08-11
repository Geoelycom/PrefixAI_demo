import requests

def get_bitcoin_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    data = response.json()
    return data["bpi"]["USD"]["rate"]

if __name__ == "__main__":
    print(f"Current Bitcoin Price: ${get_bitcoin_price()}")