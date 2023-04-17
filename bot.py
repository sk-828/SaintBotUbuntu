# coding: utf-8
from discord.ext import commands

bot = commands.Bot(command_prefix='$')


@bot.command(name="こんにちは")
async def hello(ctx):
    await ctx.send(f"どうも、{ctx.message.author.name}さん！")


@bot.command(name="さようなら")
async def goodbye(ctx):
    await ctx.send(f"じゃあね、{ctx.message.author.name}さん！")


# 取得したトークンを「TOKEN_HERE」の部分に記入
bot.run('NzUxMzQ1NjEzNTEzNDI0OTQ4.X1HvIQ.4lbbjmChjXBcSVeD4m1RP7QnO5o')