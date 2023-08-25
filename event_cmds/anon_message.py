import discord
import settings
from discord.ext import commands
from discord.ui import Button, View, Modal, TextInput

class AnonModal(Modal, title="Send an anonymous message."):
    anon_message = TextInput(
        style=discord.TextStyle.short,
        label="Anonymous Message",
        required=True,
        placeholder="Ackkk eto na aamin na ko sayo, aywavyou!! (´▽`ʃ♡ƪ)",
    )

    # I don't know if I should add an alias/penname for the anonymous message
    # nickname = TextInput(
    #     style=discord.TextStyle.short,
    #     label="Alias",
    #     required=False,
    #     placeholder="super cute",
    # )

    async def on_submit(self, interaction) -> None:
        user = interaction.user

        # Create an embed of the anonymous message
        embed = discord.Embed(description=f"{self.anon_message}", color=discord.Color.pink())
        await interaction.channel.send(embed=embed)

        # with open(str(settings.LOGS_DIR / "anon.txt"), "a") as file:
        #     file.write(
        #         f"User: '{user.name}' | ID: '{user.id}' | Message: '{self.anon_message}'\n\n"
        #     )

        async for message in interaction.channel.history(limit=None):
            if message.components:
                await message.delete()

        await interaction.response.send_message(f"{user.name}, your message has been sent.", ephemeral=True)
        # await interaction.response.defer() #this will not display any message

    async def on_error(self, interaction, error: Exception) -> None:
        return await super().on_error(interaction, error)
    

async def anon_message(bot: commands.Bot):
    anon_channel = bot.get_channel(settings.ANON_CHANNEL_TOKEN)

    async for message in anon_channel.history(limit=None):
            if message.components:
                await message.delete()

    async def button_callback(interaction):
        await interaction.response.send_modal(AnonModal())

    embed = discord.Embed(
        title='Sneaky Alf',
        description='Click the button down below to send an anonymous message!',
        color=discord.Color(0xFF69B4)
    )

    verify_button = Button(style=discord.ButtonStyle.primary, label="🤫 Confess")
    verify_button.callback = button_callback
    view = View()
    view.add_item(verify_button)

    await anon_channel.send(embed=embed, view=view)

"""
things to do:
fix the embed - done
learn the sticky message for the anon button - done
call the function every 10 minutes to avoid the "this interaction failed" - done
maybe mute the notification of the bot for everyone? 
"""
