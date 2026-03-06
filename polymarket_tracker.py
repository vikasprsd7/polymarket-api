import requests

BASE_URL = "https://clob.polymarket.com"
GAMMA_URL = "https://gamma-api.polymarket.com"

def get_active_markets():
    response = requests.get(f"{GAMMA_URL}/markets?active=true&closed=false")
    return response.json()

def get_resolved_markets():
    response = requests.get(f"{GAMMA_URL}/markets?closed=true")
    return response.json()

def get_order_book(token_id):
    response = requests.get(f"{BASE_URL}/book?token_id={token_id}")
    return response.json()

def get_market_categories():
    response = requests.get(f"{GAMMA_URL}/markets?category=politics")
    return response.json()

if __name__ == "__main__":
    markets = get_active_markets()
    print(markets)