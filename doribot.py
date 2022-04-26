# THE CODE IS NOT FULLY COMPLETED.

import discord
import wikipedia, datetime
from gnewsclient import gnewsclient

bot = discord.Bot(debug_guilds=[]) # specify the guild IDs in debug_guilds


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")



@bot.command(description="Sends the bot's latency.") # this decorator makes a slash command
async def ping(ctx): # a slash command will be created with the name "ping"
    await ctx.respond(f"Pong! Latency is int({bot.latency})")




class View(discord.ui.View): # Create a class called View that subclasses discord.ui.View
    @discord.ui.button(label="Click me!", style=discord.ButtonStyle.primary, emoji="😎") # Create a button with the label "😎 Click me!" with color Blurple
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("You clicked the button!") # Send a message when the button is clicked

@bot.slash_command()
async def bttn(ctx):
    await ctx.respond("This is a button!", view=View()) # Send a message with our View class that contains the button


@bot.slash_command(description="Get the Breaking News using Google News.")
async def news(ctx, lang: discord.Option(str), country: discord.Option(str), tematic: discord.Option(str)):
    client = gnewsclient.NewsClient(language=lang,
	    							location=country,
    								topic=tematic,
    								max_results=3)

    news_list = client.get_news()
    embed = discord.Embed(title=f":newspaper: Google News API", description=f"Breaking news of {country} in {tematic} topic.", color=0xe2be5a, url="https://news.google.com")
    for item in news_list:
        embed.add_field(name=f":newspaper2: Breaking news", value= f"{item['title']} - [Link]({item['link']})")
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text='Google News')
    await ctx.respond(embed=embed)
