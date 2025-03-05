import requests
import schedule
import time

# Your bot token and chat ID
BOT_TOKEN = ""
CHAT_ID = ""

# Function to get Bitcoin price
def get_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url).json()
    return response["bitcoin"]["usd"]

# Function to send a message
def send_message():
    price = get_bitcoin_price()
    text = f"Bitcoin Price: ${price}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}"
    requests.get(url)

# Schedule the bot to run every 10 minutes
schedule.every(10).minutes.do(send_message)

send_message()  # Send the first message immediately

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
