import requests
import sys

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
response.raise_for_status()
data = response.json()

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")

elif not sys.argv[1][0].isdigit():
    sys.exit("command-line argument is not a number")

else:
    number = float(sys.argv[1])
    try:
        amount = float(data["bpi"]["USD"]["rate_float"]) * number
        print(f"${amount:,.4f}")

    except requests.RequestException:
        sys.exit("Try again")


