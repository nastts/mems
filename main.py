import discord
from discord.ext import commands 
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)


@bot.command()
async def mem(ctx):
    img_lst = os.listdir('images')
    with open(f'images/{random.choice(img_lst)}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
@bot.command()
async def animals(ctx):
    img_lst2 = os.listdir('animals')
    with open(f'animals/{random.choice(img_lst2)}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


bot.run('токен')
