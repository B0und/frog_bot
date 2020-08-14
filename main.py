import discord
from discord.ext import commands
import os, random
from dotenv import load_dotenv
import pathlib


load_dotenv()
TOKEN = os.environ['TOKEN']
BOT_PREFIX = '!'

pics_dir = pathlib.Path("pics")
bot = commands.Bot(command_prefix=BOT_PREFIX)
pic_list = []

def init_pics():
    global pic_list
    pic_list = os.listdir(pics_dir)
    random.shuffle(pic_list)


@bot.event
async def on_ready():
    global pic_list
    init_pics()
    activity = discord.Game(name="!toad")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print('We have logged in as {0.user}'.format(bot))


@bot.command(pass_context=True, aliases=['жаба', 'ристик'])
@commands.cooldown(1, 0.5, commands.BucketType.guild)
async def toad(ctx):
    global pic_list
    last_pic = pic_list[-1] 
    pic_list.pop()
    if len(pic_list) == 0:
        init_pics()
    await ctx.message.channel.send(file=discord.File(pathlib.Path(pics_dir, last_pic)))


bot.run(TOKEN)