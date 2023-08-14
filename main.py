import settings
import discord
import random
import asyncio
from stay_alive import stay_alive
from discord.ext import commands


async def verification_message(bot):
  channel = bot.get_channel(settings.VERIFY_CHANNEL_TOKEN)

  # Clear the channel
  async for message in channel.history(limit=None):
    await message.delete()

  # Send message
  message = await channel.send("React here to get verified ૮꒰˶ᵔ ᵕ ᵔ˶ ꒱ა")
  await message.add_reaction("\u2705")


async def chat_user(bot, user):

  def check(msg):
    return msg.author == user and isinstance(msg.channel, discord.DMChannel)

  try:
    await user.send("Hi there! What's your full name?")
    response = await bot.wait_for("message", check=check, timeout=300.0)
    name = response.content

    await user.send(
      "Please give me your AWS CC Membership ID or Personal Gmail ૮꒰˶ᵔ ᵕ ᵔ˶ ꒱ა"
    )
    response = await bot.wait_for("message", check=check, timeout=300.0)
    proof = response.content
  except asyncio.TimeoutError:
    await user.send(
      "You took too long to respond. Please try again by reacting once more.")
    return None, None

  await user.send(
    "Thank you for replying ૮꒰˶ᵔ ᵕ ᵔ˶ ꒱ა\nIf you mistyped your response, you can try again by reacting once more to my message.\nPlease wait while our moderators verify your account."
  )
  return name, proof


def run():
  intents = discord.Intents.all()

  bot = commands.Bot(command_prefix="@", intents=intents)

  @bot.event
  async def on_ready():
    print(f"User: {bot.user} (ID: {bot.user.id})")
    await verification_message(bot)

  @bot.event
  async def on_member_join(member):
    welcome_channel = bot.get_channel(settings.WELCOME_CHANNEL_TOKEN)
    custom_messages = [
      f"{member.name} has joined the server!",
      f"Hi {member.mention}, welcome to the server!"
    ]

    await welcome_channel.send(random.choice(custom_messages))

  @bot.event
  async def on_reaction_add(reaction, user):
    if user != bot.user:  # Ignore reactions from the bot itself
      message = reaction.message

      # DM user and ask for name or ID
      name, proof = await chat_user(bot, user)

      if name is not None and proof is not None:
        # Insert into text file
        with open("verify.txt", "a") as f:
          f.write(
            f"User: {user.name} | ID: {user.id} | Nickname: {user.nick} Name: {name} | Proof: {proof}\n"
          )

      # Remove user's reaction para clean
      await message.remove_reaction("\u2705", user)

  bot.run(settings.TOKEN)


if __name__ == "__main__":
  stay_alive()
  run()
