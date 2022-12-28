import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from time import sleep
import math
from threading import Thread
import string

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
    if(not sleeping):
        set_pin(1)
        sleep(0.1)

def off():
    if(not sleeping):
        set_pin(0)
        sleep(0.1)

def gm():
    on()
    sleeping = False

def gn():
    off()
    sleeping = True

def reboot():
    os.popen('sudo reboot')


@client.event
async def on_ready():
    on()
    print('bot ready')

@client.event
async def on_message(message):
    
    content = (message.content).lower()
    author = message.author.name
    
    if 'melfie' in author:
        sleeping = False
        if(content == 'gn' or content == 'off'):
            gn()

        if(content == 'on'):
            gm()

    if(content == 'imy' or content == 'wyd' or content == 'hyd'):
        print('sending love')
        blink()
    
    if(content == 'mwah' or content == 'ily'):
        print('sending love')
        heartbeat()

    
    


    if(content == 'lamp off'):
        gn()
        
    if(content == 'lamp reboot'):
        reboot()
        
    print(author, content)


client.run(TOKEN)

