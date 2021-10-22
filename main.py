import discord
from discord.ext import commands
import dotenv
from dotenv import load_dotenv
import os

load_dotenv()
#import all of the cogs
from commands import main_cog
#from image_cog import image_cog
from play import music_cog

bot = commands.Bot(command_prefix='>')

#remove the default help command so that we can write out own
bot.remove_command('help')

#register the class with the bot
bot.add_cog(main_cog(bot))
#bot.add_cog(image_cog(bot))
bot.add_cog(music_cog(bot))

@bot.event
async def on_ready():
    print('Hello, I am your music bot {0.user}'
    .format(bot))
    general_channel= bot.get_channel(882939306870714408)

    await general_channel.send('Hello, I am your music bot {0.user}'
    .format(bot))

#start the bot with our token
bot.run(os.getenv('TOKEN'))