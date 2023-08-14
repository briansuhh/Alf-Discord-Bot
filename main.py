import settings
import discord
import random
from stay_alive import stay_alive
from discord.ext import commands

def run():
    intents = discord.Intents.all()
    
    bot = commands.Bot(command_prefix="@", intents=intents)

    @bot.event
    async def on_ready():
        # Load commands
        for cmd in settings.CMDS_DIR.glob("*.py"):
            if cmd.name != "__init__.py":
                await bot.load_extension(f"cmds.{cmd.name[:-3]}")
            
        # Load Cogs
        for cog in settings.COGS_DIR.glob("*.py"):
            if cog.name != "__init__.py":
                await bot.load_extension(f"cogs.{cog.name[:-3]}")
        
        print(f"User: {bot.user} (ID: {bot.user.id})")

    @bot.event
    async def on_member_join(member):
        welcome_channel = bot.get_channel(1106761390397587558)
        custom_messages = [
            f"{member.name} has joined the server!",
            f"Hi {member.mention}, welcome to the server!"
        ]

        await welcome_channel.send(random.choice(custom_messages))
    
    @bot.command()
    async def reload_bot(ctx):
        # Reload commands
        for cmd in settings.CMDS_DIR.glob("*.py"):
            if cmd.name != "__init__.py":
                await bot.reload_extension(f"cmds.{cmd.name[:-3]}")
            
        # Reload Cogs
        for cog in settings.COGS_DIR.glob("*.py"):
            if cog.name != "__init__.py":
                await bot.reload_extension(f"cogs.{cog.name[:-3]}")

        await ctx.send("Reload complete!")
    
    bot.run(settings.TOKEN)

if __name__ == "__main__":
    stay_alive()
    run()