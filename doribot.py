## Here start my beutiful code :3

import discord
from gnewsclient import gnewsclient
import wikipedia
import os
import time
import discord
import random
import asyncio
from mcstatus import MinecraftServer
import re

from forex_python.bitcoin import BtcConverter

import requests
from bs4 import BeautifulSoup
from PyDictionary import PyDictionary
from translate import Translator
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
import datetime

token = "TOKEN"

async def is_owner(ctx):
    return ctx.author.id == 841368898146402355 # Dorikyh#0018 ID

hos = 0
arg = ""
clim = ""

client = discord.Client()
client = commands.Bot(command_prefix = '*')
client.remove_command('help')

user = discord.utils.get(client.get_all_members(), id='1234')

@client.event
async def on_ready():
    print(f"\n==================\nBot online!\nLogged as: {client.user.name}\n==================\n")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='*cmd'))

@client.command()
async def cmd(ctx):
    embed = discord.Embed(title=":gear: Page 1 | Bot prefix: `*`",
    description="Global command list bot available.", color=0x8ee5ee)
    embed.set_author(name="Doribot | User command list" , icon_url="https://i.ibb.co/RjSB9LD/external-content-duckduckgo.png")
    
    embed.add_field(name=":newspaper: News", value="Get the breaking news of your city.")
    embed.add_field(name=":scroll: Wiki_en", value="English search in wikipedia.")
    embed.add_field(name=":scroll: Wiki_es", value="Spanish search in wikipedia.")
    embed.add_field(name=":cloud: Climate", value="Google weather API.")
    embed.add_field(name=":flag_us: To_en", value="Translate spanish to english.")
    embed.add_field(name=":flag_es: To_es", value="Translate english to spanish.")

    embed.set_footer(text='Use info <cmd> to get more info.')
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)
    print("[EXC] General help list 1")




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
    print("[EXC] Admin help list 1")




@client.command()
async def cmd2(ctx):
    embed = discord.Embed(title=":gear: User command list page 2",
    description="User command list available. \nThe command prefix is `*` (Do not use caps)", color=0x8ee5ee)

    embed.add_field(name=":coin: CoinFlip", value="Heads or tails random gen.")
    embed.add_field(name=":1234: Randint", value="Random number, 0 up 100.")
    embed.add_field(name=":coin: BTC", value="Get the bitcoin value.")
    embed.add_field(name=":zero: Binary", value="Convert text to binary.")
    embed.add_field(name=":u7a7a: ASCII", value="Text to ASCII code.")
    embed.add_field(name=":ping_pong: MCServ", value="Minecraft server status.")

    embed.set_footer(text='Use .info <cmd> to get more info.')
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)
    print("[EXC] General help list 2")



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
    print(f"[EXC] Coinflip: {hos}")

county = 0

@client.command()
async def count(ctx):
    global county
    county = county + 1 
    embed = discord.Embed(title=f":small_red_triangle: +1 Count!", description=f"Now counter is: {county}", color=0x808080)
    print(f"Count command: {county}")
    await ctx.send(embed=embed)
    print(f"[EXC] Count: {county}")



@client.command()
async def mcserv(ctx, *, arg1):
    server = MinecraftServer.lookup(arg1)

    status = server.status()
    embed = discord.Embed(title=f":ping_pong: Minecraft server {arg1}", description=f"The server {arg1} has {status.players.online} players online, server replied in {int(status.latency)}ms", color=0x77dd77)
    embed.set_footer(text='MCStatus')
    embed.set_author
    if int(status.latency) <= 1:
        print("error")
    else:
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
        print(f"[EXC] MCServ: {arg1} {status.players.online} {status.latency}")


@client.command()
async def uncount(ctx):
    global county
    county = county - 1 
    embed = discord.Embed(title=f":small_red_triangle_down: -1 Count!", description=f"Now counter is: {county}", color=0x808080)
    await ctx.send(embed=embed)
    print(f"[EXC] Uncount: {county}")

@client.command()
async def randint(ctx):
    ran = random.randint(0, 100)
    embed = discord.Embed(title=f"Random number: {ran}", description=f"This result has been randomly generated.", color=0xffffed)
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)
    print(f"[EXC] Randint: {ran}")



@client.command()
async def bin(ctx, *, args):
    if len(args) <= 255:
        res = ''.join(format(ord(i), '08b') for i in args)

        embed = discord.Embed(title=f":zero: Binary convert", description=f"```{res}```", color=0xffffed)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
        print(f"[EXC] Binary: {args}")

    else:
        embed = discord.Embed(title=f":no_entry_sign: Error", description=f"The text entered is too long.", color=0xffffed)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
        print(f"[ERR] Too much text")


@client.command()
async def ping(ctx):
    embed = discord.Embed(title=f"Pong!  🏓 {arg}", description=f":bell: {round(client.latency * 1000)}ms", color=0xf28f18)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_image(url="https://www1-lw.xda-cdn.com/files/2017/05/stack-overflow.png")
    await ctx.send(embed=embed)
    print(f"[EXC] Ping: {round(client.latency * 1000)}ms.")



@client.command()
async def niwi(ctx):
    client = gnewsclient.NewsClient(language="spanish",
	    							location="colombia",
    								topic="politics",
    								max_results=1)

    newz = client.get_news()
    embed = discord.Embed(title=f":newspaper: {newz['title']}", description=f"{newz['description']}", color=0xe2be5a)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_image(url=f"{newz['image']}")
    embed.set_footer(text='Google News')
    print(f"[EXC] GNews testing")
    await ctx.send(embed=embed)


@client.command()
async def testing(ctx):
    embed = discord.Embed(title=f"Daily newsletter", description=f"Daily newsletter with useful information, breaking news and more.", color=0xf28f18)
    embed.timestamp = datetime.datetime.utcnow()
    
    b = BtcConverter() # force_decimal=True to get Decimal rates
    val = "{:,.2f}".format(b.get_latest_price('USD'))
    
    embed.add_field(name="Bitcoin value", value="Right now the bitcoin value is: ${val}")
    
    await ctx.send(embed=embed)


# sending dm
@client.command()
async def nwsletter(ctx):
    await ctx.author.send('Boop!!')



@client.command()
async def news(ctx, arg1, arg2, arg3):
    client = gnewsclient.NewsClient(language=arg1,
	    							location=arg2,
    								topic=arg3,
    								max_results=3)

    news_list = client.get_news()
    embed = discord.Embed(title=f":newspaper: Google News API", description=f"Breaking news of {arg2} in {arg3} topic.", color=0xe2be5a, url="https://news.google.com")
    for item in news_list:
        embed.add_field(name=f":newspaper2: Breaking news", value= f"{item['title']} - [Link]({item['link']})")
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Google News')
    print(f"[EXC] GNews: {arg2}")
    await ctx.send(embed=embed)



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
    print(f"[EXC] WikiEn: {rslt.title}")


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
    print(f"[EXC] Weather: {city}")



@client.command()
async def btc(ctx):
    b = BtcConverter() # force_decimal=True to get Decimal rates
    val = "{:,.2f}".format(b.get_latest_price('USD'))
    embed=discord.Embed(title=f":chart: Bitcoin value ", description=f"Right now the bitcoin value is: ${val}", color=0xb3e6b5)
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)
    print(f"[EXC] BTC: {val}")

@client.command()
@commands.check(is_owner)
async def clear(ctx , amount=5):
    await ctx.channel.purge(limit=amount + 1)
    embed=discord.Embed(title=f":wastebasket: Delete command", description=f"You have been deleted {amount} messages.", color=0xFF4C4C)
    await ctx.send(embed=embed, delete_after=3)
    print(f"[EXC] Clear: {amount}")



@client.command()
async def wiki_es(ctx, *, args):
    wikipedia.set_lang("es")
    result = wikipedia.summary(args, sentences=2)
    rslt = wikipedia.page(args)
    embed=discord.Embed(title=f":scroll: Wikipedia: {rslt.title}", url=rslt.url, description=f"{result}", color=0xe2be5a)
    embed.set_author(name="Doribot | Spanish Wikipedia" , icon_url="https://i.ibb.co/RjSB9LD/external-content-duckduckgo.png")
    embed.set_thumbnail(url="https://clipground.com/images/wikipedia-logo-7.png")
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Wikipedia API')
    await ctx.send(embed=embed)
    print(f"[EXC] WikiEs: {rslt.title}")

@client.command()
async def to_es(ctx, *, args):
    translator= Translator(from_lang="english",to_lang="spanish", provider="mymemory")
    translation = translator.translate(args)
    embed = discord.Embed(title=f":flag_us: Traduction", description=f"```{translation}```", color=0x405fdd)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Google_Translate_logo.svg/2048px-Google_Translate_logo.svg.png")
    embed.set_footer(text='Google Translate API')
    await ctx.send(embed=embed)
    print(f"[EXC] ToEs: {args}")



@client.command()
async def to_en(ctx, *, args):
    translator= Translator(from_lang="spanish",to_lang="english")
    translation = translator.translate(args)
    embed = discord.Embed(title=f":flag_us: Traduction", description=f"```{translation}```", color=0x405fdd)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Google_Translate_logo.svg/2048px-Google_Translate_logo.svg.png")
    embed.set_footer(text='Google Translate API')
    await ctx.send(embed=embed)
    print(f"[EXC] ToEn: {args}")


@client.command()
async def ascii(ctx, *, args):
    ascii_values = []
    for character in args:
        ascii_values.append(ord(character))

    embed = discord.Embed(title=f":u7a7a: Text to ASCII", description=f"```{ascii_values}```", color=0x405fdd)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='ASCII Translate')
    await ctx.send(embed=embed)
    print(f"[EXC] ASCII: {args}")


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
        print(f"[EXC] Info Wiki")


    elif arg == "news":
        embed = discord.Embed(title=f"Google News command help", description=f"Get the breaking news command.", color=0x66cccc)
        embed.add_field(name="Use Google News with commands", value="<> Required text field.\n {} Optional text field.", inline=False)
        embed.add_field(name="Command use", value="`*news <lang> <region> <topic>`",  inline=False)
        embed.add_field(name="Available topics", value="World, nation, bussines, technology,\n entertainment, sports, science & healt.",  inline=False)
        embed.set_thumbnail(url="https://cdn.freelogovectors.net/wp-content/uploads/2020/11/google-news-logo-768x629.png")

        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text='Wikipedia API command help.')
        await ctx.send(embed=embed)
        print(f"[EXC] Info GNews")


    elif arg == "to_es" or arg == "to_en": # Translate command
        embed = discord.Embed(title=f"Translate command help", description=f"Treanslate texts with commands.", color=0x66cccc)
        embed.add_field(name="Translate with commands", value="<> Required text field.\n {} Optional text field.", inline=False)
        embed.add_field(name="Command use", value="`*to_es <text>`\n `*to_en <text>`",  inline=False)
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Google_Translate_logo.svg/2048px-Google_Translate_logo.svg.png")

        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text='Google Translate command help.')
        await ctx.send(embed=embed)
        print(f"[EXC] Info ToEs")


    elif arg == "climate" or arg == "weather": # Weather command set
        embed = discord.Embed(title=f"Weather command help", description=f"Get the weather of a city with commands.", color=0x66cccc)
        embed.add_field(name="Weather with commands", value="<> Required text field.\n {} Optional text field.", inline=False)
        embed.add_field(name="Command use", value="`*climate <city>`",  inline=False)
        embed.set_thumbnail(url="http://icons.iconarchive.com/icons/iynque/ios7-style/1024/Weather-icon.png")

        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text='Google Weather command help.')
        await ctx.send(embed=embed)
        print(f"[EXC] Info climate")


@client.command(name='eval')
@commands.check(is_owner)
async def _eval(ctx, *, code):
    embed = discord.Embed(title=f"Eval code", description=f":symbols: **Input:** ```{code}```\n:arrow_right: **Output**: ```{eval(code)}```", color=0xccc9ca)
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)
    print(f"[EXC] Eval: {code}")

client.run((token))  