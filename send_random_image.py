import requests

from telegram import Bot
from muterobot import TOKEN, CHAT_ID


bot = Bot(token=TOKEN)
URL = 'https://api.thecatapi.com/v1/images/search'
response = requests.get(URL).json()
print(response)
print(type(response))
print(len(response))
print(type(response[0]))

# URL = 'https://cdn2.thecatapi.com/images/3dl.jpg'

# chat_id = CHAT_ID

# text = 'Telegram for you'

# bot.send_message(chat_id, text)
# bot.send_photo(chat_id, URL)
