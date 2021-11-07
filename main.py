# git clone https://github.com/JakinChan200/CutieHack2021.git
# ls CutieHack2021

import requests


import discord
import random
from discord.ext import commands


bot = commands.Bot(command_prefix = '-')
bot.remove_command("help")
#discordTag = ctx.author.name + "#" + ctx.author.discriminator
#await ctx.send(msg)

@bot.event
async def on_ready():
    print("nikhil sucks")
    #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening ,name="$help"))
    await bot.change_presence(activity = discord.Streaming(name = "cutiehack2021", url = "https://www.twitch.tv/monketech"))


@bot.command()
async def help(ctx):
    helpEmbed = discord.Embed(
      title = "**:tangerine: Commands :tangerine:**",
      colour=0xFF7CEF
    )

    helpEmbed.add_field(name = "COOL STUFF", value = "`-nick <nickname>\n-rand <low> <high>\n-eightball\n-quote`", inline=True)
    helpEmbed.set_thumbnail(url = 'https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/challenge_thumbnails/001/703/824/datas/original.png')

    helpEmbed.set_footer(text="Made by Jakin - Jamin - Nikhil - Steven")

    await ctx.send(embed=helpEmbed) 



@bot.command()
async def nick(ctx, member : discord.Member , *nick):
    nickname = " ".join(nick)
    await member.edit(nick = nickname)
    await ctx.send("DONE :white_check_mark:")


@bot.command()
async def rand(ctx, low, high):
    msg = random.randint(int(low), int(high))
    await ctx.send(msg)


@bot.command()
async def trivia(ctx): 
    url = "https://webknox-trivia-knowledge-facts-v1.p.rapidapi.com/trivia/search"
    querystring = {"topic":"random"}
    headers = {
    'x-rapidapi-host': "webknox-trivia-knowledge-facts-v1.p.rapidapi.com",
    'x-rapidapi-key': "dde1265195msh494dca59db22928p1f7ffcjsn3aaf27dd8d6e"
    }
    req = requests.request(url, headers = headers, params=querystring)
    await ctx.send(req.text)
    
    # "grabs api data from a trivia website and then people can respond to the question, with the final answer being given after some time"
    # "maybe given after whoever gets it correct first idk"

@bot.command()
async def eightball(ctx):
    ans = ''
    msg = random.randint(0, 6)
    if msg == 0:
        ans = 'Yes'
    elif msg == 1:
        ans = 'No'
    elif msg == 2:
        ans = 'Maybe'
    elif msg == 3:
        ans = 'Certainly'
    elif msg == 4:
        ans = 'IDK :man_shrugging:'
    elif msg == 5:
        ans = 'Ask Again'
    elif msg == 6:
        ans = 'Ask Someone Else'
    await ctx.send(ans)



@bot.command()
async def quote(ctx):
    quotes_list = ["It always seems impossible until it is done. - Nelson Mandela", 
    "When something is important enough, you do it if the odds are not in your favor - Elon Musk",
    "If you can dream it, you can do it. - Walt Disney",
    "Look up at the stars and not down at your feet. Try to make sense of what you see, and wonder about what makes the universe exist. Be curious. - Stephen Hawking",
    "A good plan violently executed now is better than a perfect plan executed next week. - George S. Patton", 
    "With the new day comes new strength and new thoughts. - Eleanor Roosevelt",
    "Our greatest glory is not in never falling, but in rising every time we fall. - Confucius",
    "We must accept finite disappointment, but never lose infinite hope. - MLK",
    "There is always room at the top. - Daniel Webster", 
    "If you don't ask, you don't get. - Stevie Wonder"
    "Spread love everywhere you go. - Mother Teresa"]

    quotes_portaits = ["https://cdn.discordapp.com/attachments/901674982843752458/906718403933384735/10Facts_Featured.png", 
    "https://cdn.discordapp.com/attachments/901674982843752458/906718689255096361/gettyimages-1229892983-square.png",
    "https://cdn.discordapp.com/attachments/901674982843752458/906718891869360189/WaltDisney.png",
    "https://cdn.discordapp.com/attachments/901674982843752458/906719123134894100/Hawking_1300Lede_LessDeep1.png",
    "https://cdn.discordapp.com/attachments/901674982843752458/906719248846561300/George-S-Patton-1945.png", 
    "https://cdn.discordapp.com/attachments/901674982843752458/906719379339743252/Eleanor-Roosevelt-1950.png",
    "https://cdn.discordapp.com/attachments/901674982843752458/906719466493194250/2Q.png",
    "https://cdn.discordapp.com/attachments/901674982843752458/906719549611728916/Z.png",
    "https://cdn.discordapp.com/attachments/901674982843752458/906719636492525598/9k.png", 
    "https://cdn.discordapp.com/attachments/901674982843752458/906719726263238676/Z.png",
    "https://cdn.discordapp.com/attachments/901674982843752458/906719816998592562/images.png"]
    
    random_int = random.randint(0,len(quotes_list))
    msg = quotes_list[random_int]
    picturelink = quotes_portaits[random_int]

    quoteEmbed = discord.Embed(
      title = "**Here Ya Go! :smile:**",
      colour=0xFF7CEF
    )

    quoteEmbed.add_field(name = "Quote: ", value = "***" + msg + "***", inline=True)
    quoteEmbed.set_thumbnail(url = picturelink)
    quoteEmbed.set_footer(text="Made by Jakin - Jamin - Nikhil - Steven")

    await ctx.send(embed=quoteEmbed) 



@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    if "hi" in message.content.lower() or "hello" in message.content.lower():
        #print("Hello!")
        #or
        await message.channel.send("Hello " + str(message.author.name) + '!')

    if "goodbye" in message.content.lower() or 'bye' in message.content.lower():
        #print("Bye Bye!")
        #or
        await message.channel.send("Bye Bye " + str(message.author.name + '!'))

    await bot.process_commands(message)


bot.run("OTA2NTU5MTg5MzY5OTA1MjQy.YYaZCQ.bxVm0g8pDryuvCSNcmH4Jj-swmw")
