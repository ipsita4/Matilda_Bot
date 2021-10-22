import discord
from discord.ext import commands
from discord.ext.commands.bot import Bot


class main_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = """
```
Here are all my commands:
>help - displays all the available commands.
>p <keywords> - plays your requested music.
>q - displays the current music queue.
>skip - skips the current song being played.
>clear amount - will delete the past messages with the amount specified.
>stop - This command stops the music and makes the bot leave the voice channel.
```
"""
        self.text_channel_list = []

    # some debug info so that we know the bot has started
    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_list.append(channel)

        # await self.send_to_all('Hello')

    @commands.command(name="help", help="Displays all the available commands")
    async def help(self, ctx):
        await ctx.send(self.help_message)

    async def send_to_all(self, msg):
        for text_channel in self.text_channel_list:
            await text_channel.send(msg)

    @commands.command(name="clear", help="Clears a specified amount of messages")
    async def clear(self, ctx, arg):
        # extract the amount to clear
        amount = 5
        try:
            amount = int(arg)
        except Exception:
            pass

        await ctx.channel.purge(limit=amount)

    @commands.command(name='stop', help='This command stops the music and makes the bot leave the voice channel')
    async def stop(self, ctx):
        voice_client = ctx.message.guild.voice_client
        await voice_client.disconnect()
