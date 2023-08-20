from discord.interactions import Interaction
import settings
import discord
import asyncio
from discord.ext import commands
from discord.ui import Button, View, Modal, TextInput


class VerifyModal(Modal, title="Fill in the details to get verified"):
    full_name = TextInput(
        style=discord.TextStyle.short, label="Full Name", required=True, placeholder="LastName, FirstName MiddleInitial"
    )

    proof = TextInput(
        style=discord.TextStyle.short,
        label="Membership ID or Personal Gmail",
        required=True,
        placeholder="AWS-CC-2023-#### / abc@gmail.com",
    )

    async def on_submit(self, interaction) -> None:
        user = interaction.user

        # Create an embed of their response
        embed = discord.Embed(title="Verification Response", description="Here's your given response to our questions:")
        embed.add_field(name="Full Name", value=self.full_name.value, inline=False)
        embed.add_field(name="Membership ID or Personal Gmail", value=self.proof.value, inline=False)
        embed.add_field(name="Reminder", value="You may try again by resubmitting another response")
        embed.set_author(name=user.display_name)
        embed.set_thumbnail(url=str(user.display_avatar))

        # Send a DM to the user confirming their response
        await user.send(embed=embed)

        # Save their response to verify.txt
        with open(str(settings.LOGS_DIR / "verify.txt"), "a") as f:
            f.write(
                f"User: '{user.name}' | ID: '{user.id}' | Nickname: '{user.nick}' | Name: '{self.full_name}' | Proof: '{self.proof}'\n\n"
            )

        try:
            await interaction.response.send_message()
        except Exception as e:
            print(e)

    async def on_error(self, interaction, error: Exception) -> None:
        return await super().on_error(interaction, error)


async def interactive_verification_message(bot: commands.Bot):
    channel = bot.get_channel(settings.VERIFY_CHANNEL_TOKEN)

    # Clear the channel
    async for message in channel.history(limit=None):
        await message.delete()

    # Define callback
    async def button_callback(interaction):
        """
        Tip for working with interactions:
        - If you take more than 3 seconds to responsd, use interaction.response.defer() then interacion.edit_original_message()
        """
        # Create the VerifyModal
        verify_modal = VerifyModal()
        await interaction.response.send_modal(verify_modal)

    # Create the components of the View
    verify_button = Button(label="Get verified!", style=discord.ButtonStyle.primary, emoji="\u2705")
    verify_button.callback = button_callback
    view = View()
    view.add_item(verify_button)

    # Send the view
    await channel.send("Click the button down below to get verified!", view=view)
