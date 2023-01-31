from khl import bot , Bot , Message , api 
from khl.card import *
import random
import os
import time
import requests
from bs4 import BeautifulSoup

bot = Bot(token="xxx")

print("机器人已成功启动")
exp = {"root":"无限","test":999}
userk = {"root":"237938831"}

# prefixes=['召开']
@bot.command(name="GameHL")
async def help(msg : Message): #注册/help命令函数
    #await msg.ctx.channel.send("/help : 查询命令")
    hep = CardMessage(
        Card(
            Module.Header('帮助 | GameHL'),
            Module.Divider(),
            Module.Context(Element.Text("由 (met)237938831(met) 开发,  在 [Github](https://github.com/Buelie) 查看源码", type=Types.Text.KMD)),
            Module.Divider(),
            Module.Header('命令'),
            Module.Section('/GameHL : 获取帮助\n$注册 : 注册一个GHL账户\n$注销 : 注销一个GHL账号\n$经验 : 查询账号经验\n$抽奖 : 抽奖'),
            Module.Divider(),
            color='#5A3BD7'
        )
    )
    await msg.ctx.channel.send(hep)

@bot.command(name="注册",prefixes="$")
async def reg(msg : Message,name):
    exp[name] = 0
    await msg.ctx.channel.send("注册成功")

@bot.command(name="注销",prefixes="$")
async def zx(msg : Message,name):
    exp.pop(name)
    await msg.ctx.channel.send("注销成功")

@bot.command(name="增加经验",prefixes="$")
async def reg(msg : Message,name):
    if str(msg.author.id) == userk['root']:
        exp[name] += 10
        await msg.ctx.channel.send("修改成功")
    elif str(msg.author.id) != userk['root']:
        await msg.ctx.channel.send("修改失败,您没有ROOT权限")
    else:
        await msg.ctx.channel.send("修改失败,您没有ROOT权限")

@bot.command(name="经验",prefixes="$")
async def cexp(msg : Message,name):
    hep = CardMessage(
        Card(
            Module.Header('查询 | 玩家'+name+'的经验'),
            Module.Divider(),
            Module.Section("玩家"+name+"的经验为 : [ "+str(exp[name])+" ]"),
            Module.Divider(),
            Module.Context(Element.Text("由 (met)237938831(met) 开发,  在 [Github](https://github.com/Buelie) 查看源码", type=Types.Text.KMD)),
            color='#5A3BD7'
        )
    )
    await msg.ctx.channel.send(hep)

@bot.command(name="抽奖",prefixes="$")
async def hec(msg : Message): #注册/help命令函数
    #await msg.ctx.channel.send("/help : 查询命令")
    lit = ['铝热剂','牛肉罐头','黄桃罐头','压缩饼干',
           '雨伞','铁粒','塑料袋','木棍','垃圾袋','烂掉的靴子',
           '宝箱']
    nub = ['1','2','3','4','5','6','7','8','9','10','16','32','12','11','13','1','1','1','1','1','2','15','100','5','6']
    litr = random.choice(lit)
    nubr = random.choice(nub)
    hep = CardMessage(
        Card(
            Module.Header('抽奖 | 每日抽奖'),
            Module.Divider(),
            Module.Section("\n你抽中了["+litr+"]*"+nubr+"\n"),
            Module.Divider(),
            Module.Context(Element.Text("由 (met)237938831(met) 开发,  在 [Github](https://github.com/Buelie) 查看源码", type=Types.Text.KMD)),
            color='#5A3BD7'
        )
    )
    await msg.ctx.channel.send(hep)

bot.run() #启动/启动机器人
