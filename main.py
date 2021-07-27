import discord
from discord.ext import commands
import os
import random
from dotenv import load_dotenv
from discord.ext.commands import CommandNotFound

# tes test test

load_dotenv()
TOKEN = os.environ['TOKEN']
BOT_PREFIX = '!'


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
    r'https://cdn.discordapp.com/attachments/519585558075277332/744271366819151922/index.png',
    r'https://cdn.discordapp.com/attachments/519585558075277332/744271103131779154/zhaba-kurit_244949923_orig_.jpg',
    r'https://cdn.discordapp.com/attachments/519585558075277332/744247380853129259/jab1.jpeg',
    r'https://i.redd.it/u4h78s3iw4a51.jpg',
    r'https://i.imgur.com/GEhhehd.gifv',
    r'https://i.imgur.com/fT4gWYD.gifv',
    r'https://i.redd.it/i7u7my4hwyi51.jpg',
    r'https://gfycat.com/incrediblehatefulasianwaterbuffalo',
    r'https://cdn.discordapp.com/attachments/552534078134550528/746811094470754435/Qh79FhZ9cyM.jpg',
    r'https://cdn.discordapp.com/attachments/346768691830063116/745477481917710336/fb2aa0nNM6Q.jpg',
    r'https://cdn.discordapp.com/attachments/346768691830063116/746419122757304511/SEPGs71QlPs.png',
    r'https://cdn.discordapp.com/attachments/743941195998167174/746469126804996106/FOZVBxaaIGc.jpg',
    r'https://cdn.discordapp.com/attachments/674327319049011227/746707548069036102/3N6Lv7h0YRI.png',
    r'https://cdn.discordapp.com/attachments/743941195998167174/747298073868239048/zoCKf7QXYDk.jpg',
    r'https://cdn.discordapp.com/attachments/674327319049011227/748057283103031347/k8enLfUUksc.png',
    r'https://media.discordapp.net/attachments/458718128868687873/750331734955917474/118673724_329629431719296_1164601705279387741_o.png?width=583&height=540',
    r'https://cdn.discordapp.com/attachments/674327319049011227/750532079401566239/MAdji3GDJfU.png',
    r'https://media.discordapp.net/attachments/674327319049011227/750501935240577094/8nwd3Fpv_l0.png?width=806&height=703',
    r'https://cdn.discordapp.com/attachments/743941195998167174/750643043824173097/YLbNOe5a7o8.jpg',
    r'https://cdn.discordapp.com/attachments/674327319049011227/751157759013158962/oa2XyyR4wnU.png',
    r'https://cdn.discordapp.com/attachments/674327319049011227/751173523476578374/l01a7sPR3Vw.png',
    r'https://cdn.discordapp.com/attachments/480635085419315200/702586622226595900/IMG_20200421_110434_252.jpg',
    r'https://media.discordapp.net/attachments/346768691830063116/684343930296598568/IMG_20200303_121150.jpg',
    r'https://cdn.discordapp.com/attachments/346768691830063116/683288971446452224/8HZPO5iE00w.png',
    r'https://cdn.discordapp.com/attachments/346768691830063116/677193912917426205/SPOILER_z02MZYJoRpk.png',
    r'https://cdn.discordapp.com/attachments/480635085419315200/713481343174049852/0DDfQt7A53c.png',
    r'https://cdn.discordapp.com/attachments/346768691830063116/669178577106763795/to19wKZcyFM.png',
    r'https://cdn.discordapp.com/attachments/346768691830063116/611504478876729361/m0AMF7XlFhA.png',
    r'https://cdn.discordapp.com/attachments/346768691830063116/752020769621540894/utss5x8VL9k.jpg',
    r'https://cdn.discordapp.com/attachments/346768691830063116/753213241458425906/EhbbDLnXkAsbFDd.png'
  
]

toad_meme_seq = [
#     r'https://cdn.discordapp.com/attachments/519585558075277332/744271216331980810/D7fU8MKWsAA6IrH.jpg',
#     r'https://cdn.discordapp.com/attachments/519585558075277332/744271470930165784/5bd5f6f445fc409d9be4bfddd45e7372.jpg',
#     r'https://cdn.discordapp.com/attachments/519585558075277332/744271508012138606/scale_1200.webp'
]


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error


def init_pics():
    global pic_list
    pic_list = list(set(default_toad_list))
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
