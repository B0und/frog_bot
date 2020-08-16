import discord
from discord.ext import commands
import os
import random
from dotenv import load_dotenv
from discord.ext.commands import CommandNotFound

load_dotenv()
TOKEN = os.environ['TOKEN']
BOT_PREFIX = '!'

# pics_dir = pathlib.Path("pics")
bot = commands.Bot(command_prefix=BOT_PREFIX)

pic_list = []

default_toad_list = [
    r'https://cdn.discordapp.com/attachments/346768691830063116/718863919526969344/VDe4Yagq_p4.jpg',
    r'https://cdn.discordapp.com/attachments/346768691830063116/718354681188843520/40pZ4wcxtxY.jpg',
    r'https://cdn.discordapp.com/attachments/346768691830063116/718304784498556979/HZqBcaDH5cw.png',
    r'https://imgur.com/sgb8n5c',
    r'https://cdn.discordapp.com/attachments/346768691830063116/736913657719423016/unknown.png',
    r'https://cdn.discordapp.com/attachments/346768691830063116/735434099665141841/Edgz8opWkAA7Lgr.png',
    r'https://cdn.discordapp.com/attachments/346768691830063116/730746866576130088/unknown.png',
    r'https://cdn.discordapp.com/attachments/346768691830063116/730669659501756425/EcbGlfwWoAA-0C9.png',
    r'https://cdn.discordapp.com/attachments/346768691830063116/729673849754615818/unknown.png',
    r'https://tenor.com/view/kermit-dance-dance-moves-slow-dance-grooves-gif-16592599',
    r'https://media.discordapp.net/attachments/681491447219748936/741937045513043998/ezgif_com-video-to-gif_68.gif',
    r'https://tenor.com/view/h%c3%a2m-frog-toad-frog-l%e1%ba%afc-wiggle-gif-14557565',
    r'https://tenor.com/view/epic-frog-dancing-relaxing-gif-13717398',
    r'https://tenor.com/view/chillin-gif-10127369',
    r'https://tenor.com/view/bro-frogs-tree-frog-gif-5275848',
    r'https://tenor.com/view/frog-dance-frogs-dancing-excited-gif-7628390',
    r'https://cdn.discordapp.com/attachments/674327319049011227/744070348080676884/e30ee02d25a7147fd3dd36c691ed7b6a.png',
    r'https://cdn.discordapp.com/attachments/674327319049011227/744069939689685093/2c20c4b0279e59ce2092a6e488850da5.png',
    r'https://cdn.discordapp.com/attachments/674327319049011227/744069626266386452/34c1bd75cd6b3ee76c6ef9ea9432b93e.png',
    r'https://cdn.discordapp.com/attachments/674327319049011227/744069529231032330/938bbc4908ce62b1ee511ced5fe59117.png',
    r'https://cdn.discordapp.com/attachments/674327319049011227/744069407420186654/2c2b0abac62c54ebacb7df92e2bb5f82.png',
    r'https://cdn.discordapp.com/attachments/502947848116240385/686848342344335362/P__xMioG8k0.jpg',
    r'https://cdn.discordapp.com/attachments/502947848116240385/730674405360926781/unnamed.jpg',
    r'https://cdn.discordapp.com/attachments/674327319049011227/739596885052096632/1596404002.jpg',
    r'https://cdn.discordapp.com/attachments/674327319049011227/742220011439128686/1597020136.jpg',
    r'https://media.discordapp.net/attachments/674327319049011227/739886060309446958/image3-1.png',
    r'https://cdn.discordapp.com/attachments/552534078134550528/744143517210902588/G1j8s1nzGyw.png',
    r'https://cdn.discordapp.com/attachments/552534078134550528/743964579960455218/FnRe6UMZNtA.jpg',
    r'https://cdn.discordapp.com/attachments/552534078134550528/743759644035514388/exreAOggUJU.jpg',
    r'https://cdn.discordapp.com/attachments/519585558075277332/744271490178088960/maxresdefault.jpg',
    r'https://cdn.discordapp.com/attachments/519585558075277332/744271470930165784/5bd5f6f445fc409d9be4bfddd45e7372.jpg',
    r'https://cdn.discordapp.com/attachments/519585558075277332/744271366819151922/index.png',
    r'https://cdn.discordapp.com/attachments/519585558075277332/744271192495620216/1596404002.jpg',
    r'https://cdn.discordapp.com/attachments/519585558075277332/744271103131779154/zhaba-kurit_244949923_orig_.jpg',
    r'https://cdn.discordapp.com/attachments/519585558075277332/744247380853129259/jab1.jpeg'
]

toad_meme_seq = [
    r'https://cdn.discordapp.com/attachments/519585558075277332/744271216331980810/D7fU8MKWsAA6IrH.jpg',
    r'https://cdn.discordapp.com/attachments/519585558075277332/744271470930165784/5bd5f6f445fc409d9be4bfddd45e7372.jpg',
    r'https://cdn.discordapp.com/attachments/519585558075277332/744271508012138606/scale_1200.webp'
]


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error


def init_pics():
    global pic_list
    pic_list = default_toad_list
    random.shuffle(pic_list)
    rand_num = random.randint(0, len(default_toad_list))
    pic_list = pic_list[0:rand_num] + toad_meme_seq + pic_list[rand_num:]


@bot.event
async def on_ready():
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
    await ctx.send(last_pic)


bot.run(TOKEN)
