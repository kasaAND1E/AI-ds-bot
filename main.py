import discord
from discord.ext import commands
from model import get_class
from random import randint

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.comand()
async def check(ctx):
    ctx.message.attachments()
    if ctx.message.attachment:
        for attachment in ctx.message.attachment:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f'images/{file_name}')
            await ctx.send(f'сохранили картинку в images/{file_name}')
    else:
        await ctx.send('Вы забыли загрузить картинку :( )')
        await ctx.send(get_class(model_path="keras_model.h5", labels_path="labels.txt", image_path=f"images/{file_name}"))

bot.run("")