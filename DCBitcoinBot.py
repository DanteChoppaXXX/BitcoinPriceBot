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
# Set your price limits
UPPER_LIMIT = 93000  # Alert if price goes above this
LOWER_LIMIT = 84000  # Alert if price goes below this

# Function to send a message
def send_message():
    price = get_bitcoin_price()
    text = f"Bitcoin Price💲: ${price}💸"

    # Check if price crosses the set limits
    if price >= UPPER_LIMIT:
        text += "\n🚀 Bitcoin is surging! Above $93,000!"
    elif price <= LOWER_LIMIT:
        text += "\n📉 Bitcoin dropped! Below $84,000!"

    # Send message only if price crosses a limit or it's the regular update
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}"
    requests.get(url)

# Schedule the bot to run every 10 minutes
schedule.every(10).minutes.do(send_message)

send_message()  # Send the first message immediately

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
