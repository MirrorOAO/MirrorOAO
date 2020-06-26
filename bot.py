import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_erady():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(726009153436385320)
    await channel.send(f'歡迎 {member} 加入!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(726009229550288979)
    await channel.send(f'{member} 退出伺服器了!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms毫秒)')

bot.run('NjIzODIxMDgxNDI5NDA5Nzky.XvNDWQ.WqKvvXD90xofn9_L1rFuy-tLqmA')