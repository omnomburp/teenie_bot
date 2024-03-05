import discord
import ollama
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("teenie is up!")

@bot.command()
async def teenie(ctx, *args):
    user_message = " ".join(args)
    bot_response = await send_msg(user_input = user_message)
    await ctx.send(bot_response)

async def send_msg(user_input) -> str:
    response = ollama.chat(model='dolphin-phi:2.7b-v2.6-q6_K', messages=[
      {
        'role': 'user',
        'content': user_input,
      },
    ])

    return response["message"]["content"]

bot.run("your-token")
