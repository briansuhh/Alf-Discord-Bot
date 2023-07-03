import settings
import discord
import random
from discord.ext import commands

def run():
    intents = discord.Intents.all()
    
    bot = commands.Bot(command_prefix="@", intents=intents)

    @bot.event
    async def on_ready():
        print(f"User: {bot.user} (ID: {bot.user.id})")

    @bot.event
    async def on_member_join(member):
        welcome_channel = bot.get_channel(1106761390397587558)
        custom_messages = [
            f"{member.name} has joined the server!",
            f"Hi {member.mention}, welcome to the server!"
        ]

        await welcome_channel.send(random.choice(custom_messages))
    
    bot.run(settings.TOKEN)

if __name__ == "__main__":
    run()