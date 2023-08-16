import settings
import discord
import random
from stay_alive import stay_alive
from discord.ext import commands
from event_cmds.verify_user import interactive_verification_message


def run():
    intents = discord.Intents.all()

    bot = commands.Bot(command_prefix="@", intents=intents)

    @bot.event
    async def on_ready():
        print(f"User: {bot.user} (ID: {bot.user.id})")
        settings.VERIFY_MESSAGE_ID = await interactive_verification_message(bot)

    @bot.event
    async def on_member_join(member):
        welcome_channel = bot.get_channel(settings.WELCOME_CHANNEL_TOKEN)
        custom_messages = [f"{member.name} has joined the server!", f"Hi {member.mention}, welcome to the server!"]

        await welcome_channel.send(random.choice(custom_messages))

    bot.run(settings.TOKEN)


if __name__ == "__main__":
    # stay_alive()
    run()
