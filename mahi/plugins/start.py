from .. import bot 
from telethon import events
import asyncio
import time 



@bot.on(events.NewMessage(incoming=True,pattern="/start"))
async def start(event):
  await event.reply("Hello! This is Mahi_bot")
  
@bot.on(events.NewMessage(incoming=True,pattern="Hello"))
async def start(event):
  await event.reply("Hii I am Mahibot.\nHow can I help you...")
  
@bot.on(events.NewMessage(incoming=True,pattern="/eval"))
async def start(event):
  await event.reply("Hello this is eval command")


@bot.on(events.NewMessage(incoming=True,pattern="/edit"))
async def start(event):
  a=await event.reply("Get command")
  await asyncio.sleep(3)
  await a.edit("This is edited message")
  

@bot.on(events.NewMessage(incoming=True,pattern="/help"))
async def help(event):
  await event.reply("""yta 'link of the video' : for downloading song from the youtube\n\nytv 'link of the video' : for downloading video from the youtube\n\n/tr hi/en(in which language you want to translate) 'sentence'\n
   /tr hi how are you""")