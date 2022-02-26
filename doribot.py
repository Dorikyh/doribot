## Here start my beutiful code :3

from cv2 import mean

import discord
from gnewsclient import gnewsclient
import wikipedia
import os
import time
import discord
import random
import asyncio

from forex_python.bitcoin import BtcConverter

import requests
from bs4 import BeautifulSoup
from PyDictionary import PyDictionary
from translate import Translator
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
import datetime

token = "ODg5NTQwMDYyOTU2NjM0MTY0.YUiuvQ.j1LLsiZfRz8xeAjWwnD2eDiqd0A"

async def is_owner(ctx):
    return ctx.author.id == 841368898146402355 # Dorikyh#0018 ID

hos = 0
arg = ""
clim = ""

client = discord.Client()
client = commands.Bot(command_prefix = '*')
client.remove_command('help')

@client.event
async def on_ready():
    print("\n\n\nBot online!\n")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='*cmd'))

@client.command()
async def cmd(ctx):
    embed = discord.Embed(title=":gear: User command list page 1",
    description="User command list 2 available. \nThe command prefix is `*` (Do not use caps)", color=0x8ee5ee)
 
    embed.add_field(name=":newspaper: News", value="Get the breaking news of your city.")
    embed.add_field(name=":scroll: Wiki_en", value="English search in wikipedia.")
    embed.add_field(name=":scroll: Wiki_es", value="Spanish search in wikipedia.")
    embed.add_field(name=":cloud: Climate", value="Google weather API.")
    embed.add_field(name=":flag_us: To_en", value="Translate spanish to english.")
    embed.add_field(name=":flag_es: To_es", value="Translate english to spanish.")

    embed.set_footer(text='Use info <cmd> to get more info.')
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)
    print("[EXC] General help command list 1.")




@client.command()
async def acmd(ctx):
    embed = discord.Embed(title=":gear: Admin command list page 1",
    description="Admin command list available. \nThe command prefix is `*` (Do not use caps)", color=0x8ee5ee)
 
    embed.add_field(name=":wastebasket: Delete", value="Delete messages.")
    embed.add_field(name=":abacus: Eval", value="Eval process.")
    embed.add_field(name=":stopwatch: TimeWait", value="Send a message after x seconds.")
    embed.add_field(name="Soon", value="Command available soon.")
    embed.add_field(name="Soon", value="Command available soon.")
    embed.add_field(name="Soon", value="Command available soon.")

    embed.set_footer(text='Use info <cmd> to get more info.')
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)
    print("[EXC] Admin command list.")





@client.command()
async def cmd2(ctx):
    embed = discord.Embed(title=":gear: User command list page 2",
    description="User command list available. \nThe command prefix is `*` (Do not use caps)", color=0x8ee5ee)

    embed.add_field(name=":coin: CoinFlip", value="Heads or tails random gen.")
    embed.add_field(name=":1234: Randint", value="Random number, 0 up 100.")
    embed.add_field(name=":coin: BTC", value="Get the bitcoin value.")
    embed.add_field(name=":coin: ETHER", value="Get the ethereum value.")
    embed.add_field(name=":small_red_triangle: Count", value="Just count...")
    embed.add_field(name=":small_red_triangle_down: Uncount", value="Just subtract...")

    embed.set_footer(text='Use .info <cmd> to get more info.')
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)
    print("Help command page 2 executed")



@client.command()
async def coinflip(ctx):
    hos = random.randint(0, 1)
    if hos == 0:
        embed = discord.Embed(title=f":orange_circle: Random: Head!", description=f"This result has been randomly generated.", color=0xf04f08)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title=f":yellow_circle: Random: Tails!", description=f"This result has been randomly generated.", color=0xf04f08)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    print(f"Coinflip command executed: {hos}")

county = 0

@client.command()
async def count(ctx):
    global county
    county = county + 1 
    embed = discord.Embed(title=f":small_red_triangle: +1 Count!", description=f"Now counter is: {county}", color=0x808080)
    print(f"Count command: {county}")
    await ctx.send(embed=embed)


@client.command()
async def uncount(ctx):
    global county
    county = county - 1 
    embed = discord.Embed(title=f":small_red_triangle_down: -1 Count!", description=f"Now counter is: {county}", color=0x808080)
    print(f"Count command: {county}")
    await ctx.send(embed=embed)

@client.command()
async def randint(ctx):
    ran = random.randint(0, 100)
    embed = discord.Embed(title=f"Random number: {ran}", description=f"This result has been randomly generated.", color=0xffffed)
    print(f"Random int generated: {ran}")
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)







@client.command()
async def ping(ctx):
    embed = discord.Embed(title=f"Pong!  🏓 {arg}", description=f":bell: {round(client.latency * 1000)}ms", color=0xf28f18)
    await ctx.send(embed=embed)
    print("Ping command executed")


@client.command()
async def news(ctx, arg1, arg2, arg3):
    client = gnewsclient.NewsClient(language=arg1,
	    							location=arg2,
    								topic=arg3,
    								max_results=3)

    news_list = client.get_news()
    embed = discord.Embed(title=f":newspaper: Google News API", description=f"Breaking news of {arg2} in {arg3} topic.", color=0xe2be5a, url="https://news.google.com")
    for item in news_list:
        embed.add_field(name=f":newspaper2: Breaking news", value= f"{item['title']}")
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Google News')
    await ctx.send(embed=embed)
    print(f"News command executed") 



@client.command()
async def wiki_en(ctx, *, args):
    wikipedia.set_lang("en")
    result = wikipedia.summary(args, sentences=3)
    rslt = wikipedia.page(args)
    embed=discord.Embed(title=f":scroll: Wikipedia: {rslt.title}", url=rslt.url, description=f"{result}", color=0xe2be5a)
    embed.set_thumbnail(url="https://clipground.com/images/wikipedia-logo-7.png")
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Wikipedia API')
    await ctx.send(embed=embed)
    print(f"Wikipedia command executed: {args}") 


@client.command()
async def climate(ctx, *, args):
    city = args

# creating url and requests instance
    urll = f"https://www.google.com/search?q=weather+{city}"
    html = requests.get(urll).content

# getting raw data
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

# formatting data
    data = str.split('\n')
    time = data[0]
    sky = data[1]

# getting all div tag
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    strd = listdiv[5].text

# getting other required data
    pos = strd.find('Wind')
    other_data = strd[pos:]

    embed=discord.Embed(title=f":cloud: Weather command", url=urll, description=f"Showing the {city} weather", color=0xE2F0AB)
    embed.add_field(name="Temperature: ", value=f"{temp}")
    embed.add_field(name="Sky description: ", value=f"{sky}")
    embed.add_field(name="City time: ", value=f"{time}")


    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Google Weather')
    await ctx.send(embed=embed)
    print(f"Weather command executed: {args}") 



@client.command()
async def btc(ctx):
    b = BtcConverter() # force_decimal=True to get Decimal rates
    val = "{:,.2f}".format(b.get_latest_price('USD'))

    embed=discord.Embed(title=f":chart: Bitcoin value ", description=f"Right now the bitcoin value is: ${val}", color=0xb3e6b5)
    await ctx.send(embed=embed)


@client.command()
@commands.check(is_owner)
async def clear(ctx , amount=5):
    await ctx.channel.purge(limit=amount + 1)
    embed=discord.Embed(title=f":wastebasket: Delete command", description=f"You have been deleted {amount} messages.", color=0xFF4C4C)
    await ctx.send(embed=embed, delete_after=3)



@client.command()
async def wiki_es(ctx, *, args):
    wikipedia.set_lang("es")
    result = wikipedia.summary(args, sentences=2)
    rslt = wikipedia.page(args)
    embed=discord.Embed(title=f":scroll: Wikipedia: {rslt.title}", url=rslt.url, description=f"{result}", color=0xe2be5a)
    embed.set_thumbnail(url="https://clipground.com/images/wikipedia-logo-7.png")
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Wikipedia API')
    await ctx.send(embed=embed)
    print(f"Wikipedia command executed: {args}") 

@client.command()
async def to_es(ctx, *, args):
    translator= Translator(from_lang="english",to_lang="spanish", provider="mymemory")
    translation = translator.translate(args)
    embed = discord.Embed(title=f":flag_us: Traduction", description=f"```{translation}```", color=0x405fdd)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Google_Translate_logo.svg/2048px-Google_Translate_logo.svg.png")
    embed.set_footer(text='Google Translate API')
    await ctx.send(embed=embed)
    print(f"Translate command executed: {args}") 



@client.command()
async def to_en(ctx, *, args):
    translator= Translator(from_lang="spanish",to_lang="english")
    translation = translator.translate(args)
    embed = discord.Embed(title=f":flag_us: Traduction", description=f"```{translation}```", color=0x405fdd)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Google_Translate_logo.svg/2048px-Google_Translate_logo.svg.png")
    embed.set_footer(text='Google Translate API')
    await ctx.send(embed=embed)
    print(f"Translate command executed: {args}") 


@client.command()
async def info(ctx, arg):
    if arg == "wiki" or arg=="wiki_es" or arg=="wiki_en":
        embed = discord.Embed(title=f"Wikipedia command help", description=f"Read the Wikipedia.", color=0xb6fcd5)
        embed.add_field(name="Use Wikipedia with commands", value="<> Required text field.\n {} Optional text field.", inline=False)
        embed.add_field(name="Command use", value="`*wiki_en <article>`\n`*wiki_es <article>`",  inline=False)
        embed.set_thumbnail(url="https://clipground.com/images/wikipedia-logo-7.png")

        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text='Wikipedia API command help.')
        await ctx.send(embed=embed)
        print("Wiki help command executed")


    elif arg == "news":
        embed = discord.Embed(title=f"Google News command help", description=f"Get the breaking news command.", color=0x66cccc)
        embed.add_field(name="Use Google News with commands", value="<> Required text field.\n {} Optional text field.", inline=False)
        embed.add_field(name="Command use", value="`*news <lang> <region> <topic>`",  inline=False)
        embed.add_field(name="Available topics", value="World, nation, bussines, technology,\n entertainment, sports, science & healt.",  inline=False)
        embed.set_thumbnail(url="https://cdn.freelogovectors.net/wp-content/uploads/2020/11/google-news-logo-768x629.png")

        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text='Wikipedia API command help.')
        await ctx.send(embed=embed)
        print("News help command executed")


    elif arg == "to_es" or arg == "to_en": # Translate command
        embed = discord.Embed(title=f"Translate command help", description=f"Treanslate texts with commands.", color=0x66cccc)
        embed.add_field(name="Translate with commands", value="<> Required text field.\n {} Optional text field.", inline=False)
        embed.add_field(name="Command use", value="`*to_es <text>`\n `*to_en <text>`",  inline=False)
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Google_Translate_logo.svg/2048px-Google_Translate_logo.svg.png")

        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text='Google Translate command help.')
        await ctx.send(embed=embed)
        print("Translate help command executed")


    elif arg == "climate" or arg == "weather": # Weather command set
        embed = discord.Embed(title=f"Weather command help", description=f"Get the weather of a city with commands.", color=0x66cccc)
        embed.add_field(name="Weather with commands", value="<> Required text field.\n {} Optional text field.", inline=False)
        embed.add_field(name="Command use", value="`*climate <city>`",  inline=False)
        embed.set_thumbnail(url="http://icons.iconarchive.com/icons/iynque/ios7-style/1024/Weather-icon.png")

        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text='Google Weather command help.')
        await ctx.send(embed=embed)
        print("Weather help command executed")


@client.command(name='eval')
@commands.check(is_owner)
async def _eval(ctx, *, code):
    embed = discord.Embed(title=f"Eval code", description=f":white_small_square: Result: {eval(code)}", color=0xccc9ca)
    await ctx.send(embed=embed)


client.run((token))  