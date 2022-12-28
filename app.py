import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from time import sleep
import math
from threading import Thread

load_dotenv()
TOKEN = os.environ.get("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='.', intents=intents)

current = 0
sleeping = False

def set_pin(sig):
    os.popen('pigs w 16 {}'.format(sig))

def blink():
    off()
    sleep(0.4)
    on()

def heartbeat():
    off()
    sleep(.2)
    on()
    sleep(.6)
    off()
    sleep(.2)
    on()
    
def test():
    off()
    sleep(1)
    on()
    sleep(1)
    off()
    sleep(1)
    on()

def on():
    set_pin(1)
    sleep(0.1)

def off():
    set_pin(0)
    sleep(0.1)

def gm():
    sleeping = False
    on()

def gn():
    sleeping = True
    off()



@client.event
async def on_ready():
    on()
    print('bot ready')

@client.event
async def on_message(message):
    
    content = (message.content).lower()
    
    if((message.author == 'melfie#5268')):
        sleeping = False

    if(content == 'imy' or content == 'wyd' or content == 'hyd'):
        print('sending love')
        blink()
    
    if(content == 'mwah' or content == 'ily'):
        print('sending love')
        heartbeat()

    
    if((message.author == 'melfie#5268') and ((content == 'gn') or (content == 'off'))):
        gn()

    if((message.author == 'melfie#5268') and (content == 'on')):
        gm()


    if(content == 'lamp off'):
        gn()
    #print(message.author, message.content, message.channel.id)


client.run(TOKEN)

