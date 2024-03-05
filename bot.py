import discord
import ollama
import math
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
    if len(bot_response) > 2000:
        response_len = len(bot_response)
        curr_it = 2000
        count = math.floor(response_len / 2000)
        await ctx.send(bot_response[:2000])
        for i in range(count):
            await ctx.send(bot_response[curr_it:])
            curr_it = curr_it + 2000
    else:
        ctx.send(bot_response)

async def send_msg(user_input) -> str:
    response = ollama.chat(model='dolphin-phi:2.7b-v2.6-q6_K', messages=[
      {
        'role': 'user',
        'content': user_input,
      },
    ])

    return response["message"]["content"]

bot.run("your-token")
