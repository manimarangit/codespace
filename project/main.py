import requests
from datetime import datetime
from tabulate import tabulate

def fetch_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum,dogecoin",
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def display_prices(data):
    if not data:
        print("No data available")
        return
    
    table_data = []
    for crypto, info in data.items():
        price = info.get("usd", 0)
        change = info.get("usd_24h_change", 0)
        table_data.append([
            crypto.capitalize(),
            f"${price:,.2f}",
            f"{change:.2f}%"
        ])
    
    headers = ["Cryptocurrency", "Price (USD)", "24h Change"]
    print(f"\nCrypto Prices - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

def main():
    print("Fetching cryptocurrency prices...")
    data = fetch_crypto_prices()
    display_prices(data)

if __name__ == "__main__":
    main()