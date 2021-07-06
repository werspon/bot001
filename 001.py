import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="<")

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    print(f"{member}join")

bot.run("NzI5ODg2NDcyNTc2MDQxMTMx.XwPdvw.xh-JJVjgoaeI_BwWqq_ceUQT4M4")