import os
import random
import discord
import time
#from dotenv import load_dotenv
from discord.ext import commands

#load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')
TOKEN = os.environ.get('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='+')

@bot.event
async def on_ready():
	print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='time', help='Lets you know time since last you called this command.')
async def days_since(ctx):
	now = int(time.time())
	with open ('times.txt', "r") as times:
		previous = times.readline()
	with open ('times.txt', "w") as times:
		times.write(str(now))
	time_since = now - int(previous)
	await ctx.send('Seconds since last incident: {}'.format(time_since))

@bot.command(name='coin', help='Flip a coin to your Jarp.')
async def flip_coin(ctx):
	possibilities = ['Heads', 'Tails']
	result = random.choice(possibilities)
	await ctx.send(result)

@bot.command(name='quote', help='Overheard by Baker.')
async def quotes(ctx):
	with open("quotes.txt", "rb") as quotefile:
		#logic to turn text file into comma separated array of ''
		#put it in quotes array
		quotes = quotefile.read().decode(errors='ignore').splitlines()
	chosen = random.choice(quotes)
	await ctx.send(chosen)

bot.run(TOKEN)