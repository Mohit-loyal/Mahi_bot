from telethon import TelegramClient
import logging 
import time


api_id = "26826728"
api_hash = "35ca28ae08aa543bfcaba98649a7a580"
bot_token = "6026405884:AAGCRskpZ2-eyV43oi2tBk2C_Q7eKC0S-Uo"

bot = TelegramClient("Mahibot", api_id, api_hash).start(bot_token=bot_token)
