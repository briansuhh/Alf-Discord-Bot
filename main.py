import settings
import discord
import random
from stay_alive import stay_alive
from discord.ext import commands
from event_cmds.verify_user import interactive_verification_message
from event_cmds.anon_message import anon_message

def run():
    bot = commands.Bot(command_prefix="@", intents=discord.Intents.all())

    @bot.event
    async def on_ready():
        print(f"User: {bot.user} (ID: {bot.user.id})")
        await bot.tree.sync()
        settings.VERIFY_MESSAGE_ID = await interactive_verification_message(bot)
        settings.ANON_MESSAGE_ID = await anon_message(bot)

    @bot.event
    async def on_message_delete(message):
        if message.channel.id == settings.ANON_CHANNEL_TOKEN:
            await anon_message(bot)

    @bot.tree.command(description="To resolve the 'this interaction failed' issue.")
    async def troubleshoot(interaction: discord.Interaction):
        await interaction.response.send_message("The bot is up and running.", ephemeral=True)

        # to fix the confession bot
        anon_channel = bot.get_channel(settings.ANON_CHANNEL_TOKEN)
        async for message in anon_channel.history(limit=None): 
                if message.components:
                    await message.delete()
                    
        #to fix the verification bot
        await interactive_verification_message(bot) 
    
    @bot.event
    async def on_member_join(member):
        welcome_channel = bot.get_channel(settings.WELCOME_CHANNEL_TOKEN)
        custom_messages = [
            f"Holabels to the server, my lalambs {member.mention} ૮꒰˶ᵔ ᵕ ᵔ˶ ꒱ა ♡",
            f"Wazzaap, {member.mention}! ...and welcome to the most amazing org evauhh! ૮꒰˵•̀ ﻌ •´˵꒱ა",
            f"Hellow, fellow recruit {member.mention}! We've been expecting you ^^ ૮꒰ •̀⤙ •´˵꒱ა",
            f"How are you, {member.mention}? Fine, thank you~ It is good to finally have you NYAAA ૮꒰˶ᵔ ᗜ ᵔ˶ ꒱ა",
            f"Acccxk! my cloud buddy, {member.mention}, has finally arrived yaaay~ ૮₍ ˶ᵔ ᵕ ᵔ˶ ₎ა",
            f"Haeiyouuuw, {member.mention}! >< So happy to have you here now with us~ ૮꒰˶ᵔ ᵕ ᵔ˶ ꒱ა",
            f"Aiyooo, {member.mention}! -^^- Been waiting for you here for ages now, hmp! ૮꒰ •̀⤙ •´˵꒱ა",
            f"You're finally here, {member.mention}! >< Welcome to my space crew~ hehe ૮꒰˶ᵔ ᵕ ᵔ˶ ꒱ა",
            f"Elloow, {member.mention}! Took you so long to arrive, eh? ૮꒰˵•̀ ﻌ •´˵꒱ა",
            f"Emeji! That's my {member.mention} right there! Welcome aboard, my cloud bud~ ૮꒰˶ᵔ ᗜ ᵔ˶ ꒱ა",
            f"Welcome to the crew, {member.mention}!!! Are ye ready for an adventure??? ૮꒰˵•̀ ﻌ •´˵꒱ა ",
            f"Great to meet ya, mi alfaloves {member.mention}! >< You're now part of the cloud crew~ ૮꒰˶ᵔ ᵕ ᵔ˶ ꒱ა",
            f"Holler up to the newly added cloud buddy, {member.mention}! LET'S MAKE SUM NOISE~ ૮꒰˶ᵔ ᗜ ᵔ˶ ꒱ა",
            f"Hemlooo, {member.mention}!!! 'wag mo na ako iiwan, ha??? padlock tapon susi sa river mehehe ૮₍ ˶ᵔ ᵕ ᵔ˶ ₎ა",
            f"Hi, your name is (what?), your name is (who?), your name is {member.mention} and welcome to the one and only server ૮꒰˵•̀ ﻌ •´˵꒱ა",
            f"Whale-corn— ay mali... WELCOME TO THE SERVER, {member.mention} ૮꒰˶ᵔ ᵕ ᵔ˶ ꒱ა",
            f"Andito na si {member.mention} wala siyang apelyido, magbabagsakan dito in 5... 4... 3... 2...",
            f"Annyeonghaseyo, {member.mention} ♡♡♡ Are you ready to be AWSified by this server?!!",
            f"Hola, {member.mention}! miss na kita :((( AY KAKAJOIN MO LANG PALA... welcome!!! ACKXKX",
            f"Buckle up, {member.mention}! we're about to take you on a journey to reach the sky and raise the 'baa' together ૮꒰ ˶˃ ᵕ ˂˶꒱ა⸝♡",
        ]

        await welcome_channel.send(random.choice(custom_messages))

    bot.run(settings.TOKEN)


if __name__ == "__main__":
    # stay_alive()
    run()
