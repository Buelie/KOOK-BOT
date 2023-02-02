from khl import bot , Bot , Message , api 
from khl.card import *
import random
import os
import time

bot = Bot(token="1/MTM2OTk=/kqk/pdBPJwDb3DJv4SJfOA==") 

print("机器人已成功启动")

# prefixes=['召开']
@bot.command(name="GameHL")
async def help(msg : Message): #注册/help命令函数
    #await msg.ctx.channel.send("/help : 查询命令")
    hep = CardMessage(
        Card(
            Module.Header('帮助 | GameHL'),
            Module.Divider(),
            Module.Context(Element.Text("由 (met)237938831(met) 开发,\
                            在 [Github](https://github.com/Buelie/KOOK-BOT/blob/main/GameHL) 查看源码",\
                            type=Types.Text.KMD)),
            Module.Divider(),
            Module.Header('命令'),
            Module.Divider(),
                Module.Context(Element.Text("**`/GameHL` : 获取帮助\n`$注册` : 注册一个GHL账户\n`$注销` : 注销一个GHL账号\n`$经验` : 查询账号经验\n`$抽奖` : 抽奖**", type=Types.Text.KMD)),
            Module.Divider(),
            Module.Context(Element.Text("**GameHL V0.1.9更新\n* **`更新了探索机制`**\n  * **`探索成功率提高到90%,不再是一半`**\n  * **`绑定经验值系统`**\n  * **`经验值增加机制`**\n  * **`经验值访问机制`**\n  * **`增加下界维度及相关群系(荒地)`**\n* **`更新了ROOT权限`**\n* **`停止依赖第三方数据库`**", type=Types.Text.KMD)),
            color='#5A3BD7'
        )
    )
    await msg.ctx.channel.send(hep)

exp = {"root":"无限"}
userk = {"root":"237938831"}

vip = {"A-On1":"237938831"}

# 成就系统

accomplishment_ExploreMadness_finish = {"1","2"}
accomplishment_ExploreMadness = {"ROOT":15}

@bot.command(name="激活成就",prefixes="$")
async def reg(msg : Message,name,accomplishment,rot):
    if accomplishment == "探索狂魔":
        if rot == "权限激活":
            if str(msg.author.id) == userk['root']:
                accomplishment_ExploreMadness_finish.add(name)
                hep = CardMessage(
                    Card(
                        Module.Header('成就 | 激活'),
                        Module.Divider(),
                        Module.Section("玩家"+name+"成就激活成功"),
                        Module.Divider(),
                        Module.Context(Element.Text("由 (met)237938831(met) 开发, 在 [Github](https://github.com/Buelie) 查看源码", type=Types.Text.KMD)),
                        color='#5A3BD7'
                    )
                )
            elif str(msg.author.id) != userk['root']:
                hep = CardMessage(
                    Card(
                        Module.Header('成就 | 激活'),
                        Module.Divider(),
                        Module.Section("玩家"+name+"成就激活失败,原因:没有ROOT权限"),
                        Module.Divider(),
                        Module.Context(Element.Text("由 (met)237938831(met) 开发, 在 [Github](https://github.com/Buelie) 查看源码", type=Types.Text.KMD)),
                        color='#fff000'
                    )
                )
        elif rot == "激活":
            if accomplishment_ExploreMadness[name] == 15:
                hep = CardMessage(
                    Card(
                        Module.Header('成就 | 激活'),
                        Module.Divider(),
                        Module.Section("玩家"+name+"成就激活成功"),
                        Module.Divider(),
                        Module.Context(Element.Text("由 (met)237938831(met) 开发, 在 [Github](https://github.com/Buelie) 查看源码", type=Types.Text.KMD)),
                        color='#5A3BD7'
                    )
                )
            elif accomplishment_ExploreMadness[name] == 15:
                hep = CardMessage(
                    Card(
                        Module.Header('成就 | 激活'),
                        Module.Divider(),
                        Module.Section("玩家"+name+"成就激活失败,原因:条件不满足"),
                        Module.Divider(),
                        Module.Context(Element.Text("由 (met)237938831(met) 开发, 在 [Github](https://github.com/Buelie) 查看源码", type=Types.Text.KMD)),
                        color='#5A3BD7'
                    )
                )
    await msg.ctx.channel.send(hep)

# GHL账号系统

@bot.command(name="注册",prefixes="$")
async def reg(msg : Message,name):
    exp[name] = 0
    accomplishment_ExploreMadness[name] = 0
    userk[name] = str(msg.author.id)
    await msg.ctx.channel.send("注册成功")

@bot.command(name="注销",prefixes="$")
async def zx(msg : Message,name):
    exp.pop(name)
    await msg.ctx.channel.send("注销成功")

# 经验值系统

@bot.command(name="增加经验",prefixes="$")
async def reg(msg : Message,name):
    if str(msg.author.id) == userk['root']:
        exp[name] += 10
        await msg.ctx.channel.send("修改成功")
    elif str(msg.author.id) != userk['root']:
        await msg.ctx.channel.send("修改失败,您没有ROOT权限")
    else:
        await msg.ctx.channel.send("修改失败,您没有ROOT权限")

@bot.command(name="减少经验",prefixes="$")
async def reg(msg : Message,name):
    if str(msg.author.id) == userk['root']:
        exp[name] -= 10
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

# 探索系统

@bot.command(name="探索",prefixes="$")
async def cexp(msg : Message,world,name,user):
    Suc = random.randint(0,100)
    if Suc >= 10:
        Success = "成功"
    elif Suc < 10:
        Success = "失败"
    if world == "主世界":
        if name == "橡木林":
            if Success == "失败":
                hep = CardMessage(
                    Card(
                        Module.Header('探索 | 主世界'+name+'地区'),
                        Module.Divider(),
                        Module.Section("玩家"+user+"探索橡木林"+Success),
                        Module.Divider(),
                        Module.Context(Element.Text("由 (met)237938831(met) 开发,  在 [Github](https://github.com/Buelie) 查看源码", type=Types.Text.KMD)),
                        color='#5A3BD7'
                    )
                )
            elif Success == "成功":
                sl = random.randint(1,64)
                hep = CardMessage(
                    Card(
                        Module.Header('探索 | 主世界'+name+'地区'),
                        Module.Divider(),
                        Module.Section("玩家"+user+"探索橡木林"+Success+"\n获得了[树枝*"+str(sl)+"]"),
                        Module.Divider(),
                        Module.Context(Element.Text("由 (met)237938831(met) 开发,  在 [Github](https://github.com/Buelie) 查看源码", type=Types.Text.KMD)),
                        color='#5A3BD7'
                    )
                )
                exp[user] += 5
        elif name == "沙漠":
            if exp[user] >= 10:
                if Success == "失败":
                    hep = CardMessage(
                        Card(
                            Module.Header('探索 | 主世界'+name+'地区'),
                            Module.Divider(),
                            Module.Section("玩家"+user+"探索沙漠"+Success),
                            Module.Divider(),
                            Module.Context(Element.Text("由 (met)237938831(met) 开发,  在 [Github](https://github.com/Buelie) 查看源码", type=Types.Text.KMD)),
                            color='#5A3BD7'
                        )
                    )
                elif Success == "成功":
                    sl = random.randint(1,64)
                    hep = CardMessage(
                        Card(
                            Module.Header('探索 | 主世界'+name+'地区'),
                            Module.Divider(),
                            Module.Section("玩家"+user+"探索沙漠"+Success+"\n获得了[沙子*"+str(sl)+"桶]"),
                            Module.Divider(),
                            Module.Context(Element.Text("由 (met)237938831(met) 开发,  在 [Github](https://github.com/Buelie) 查看源码", type=Types.Text.KMD)),
                            color='#5A3BD7'
                        )
                    )
                    exp[user] += 5
            elif exp[user] < 10:
                hep = CardMessage(
                    Card(
                        Module.Header('探索 | 主世界'+name+'地区'),
                        Module.Divider(),
                        Module.Section("玩家"+user+"探索沙漠失败,原因:经验值不足(经验值>=10即可探索)"),
                        Module.Divider(),
                        Module.Context(Element.Text("由 (met)237938831(met) 开发,  在 [Github](https://github.com/Buelie) 查看源码", type=Types.Text.KMD)),
                        color='#5A3BD7'
                    )
                )
        elif name == "白桦林":
            if exp[user] >= 10:
                if Success == "失败":
                    hep = CardMessage(
                        Card(
                            Module.Header('探索 | 主世界'+name+'地区'),
                            Module.Divider(),
                            Module.Section("玩家"+user+"探索白桦林"+Success),
                            Module.Divider(),
                            Module.Context(Element.Text("由 (met)237938831(met) 开发,  在 [Github](https://github.com/Buelie) 查看源码", type=Types.Text.KMD)),
                            color='#5A3BD7'
                        )
                    )
                elif Success == "成功":
                    sl = random.randint(1,64)
                    hep = CardMessage(
                        Card(
                            Module.Header('探索 | 主世界'+name+'地区'),
                            Module.Divider(),
                            Module.Section("玩家"+user+"探索白桦林"+Success+"\n获得了[白桦原木*"+str(sl)),
                            Module.Divider(),
                            Module.Context(Element.Text("由 (met)237938831(met) 开发,  在 [Github](https://github.com/Buelie) 查看源码", type=Types.Text.KMD)),
                            color='#5A3BD7'
                        )
                    )
                    exp[user] += 5
            elif exp[user] < 10:
                hep = CardMessage(
                    Card(
                        Module.Header('探索 | 主世界'+name+'地区'),
                        Module.Divider(),
                        Module.Section("玩家"+user+"探索白桦林失败,原因:经验值不足(经验值>=10即可探索)"),
                        Module.Divider(),
                        Module.Context(Element.Text("由 (met)237938831(met) 开发,  在 [Github](https://github.com/Buelie) 查看源码", type=Types.Text.KMD)),
                        color='#5A3BD7'
                    )
                )
    elif world == "下界":
        if exp[user] >= 50:
            if name == "荒地":
                if Success == "失败":
                    hep = CardMessage(
                        Card(
                            Module.Header('探索 | 下界'+name+'地区'),
                            Module.Divider(),
                            Module.Section("玩家"+user+"探索荒地"+Success),
                            Module.Divider(),
                            Module.Context(Element.Text("由 (met)237938831(met) 开发,  在 [Github](https://github.com/Buelie) 查看源码", type=Types.Text.KMD)),
                            color='#5A3BD7'
                        )
                    )
                elif Success == "成功":
                    sl = random.randint(1,64)
                    hep = CardMessage(
                        Card(
                            Module.Header('探索 | 下界'+name+'地区'),
                            Module.Divider(),
                            Module.Section("玩家"+user+"探索荒地"+Success+"\n获得了[岩浆*"+str(sl)+"桶]"),
                            Module.Divider(),
                            Module.Context(Element.Text("由 (met)237938831(met) 开发,  在 [Github](https://github.com/Buelie) 查看源码", type=Types.Text.KMD)),
                            color='#5A3BD7'
                        )
                    )
                    exp[user] += 5
            if name == "地狱堡垒":
                if Success == "失败":
                    hep = CardMessage(
                        Card(
                            Module.Header('探索 | 下界'+name+'地区'),
                            Module.Divider(),
                            Module.Section("玩家"+user+"探索地狱堡垒"+Success),
                            Module.Divider(),
                            Module.Context(Element.Text("由 (met)237938831(met) 开发,  在 [Github](https://github.com/Buelie) 查看源码", type=Types.Text.KMD)),
                            color='#5A3BD7'
                        )
                    )
                elif Success == "成功":
                    sl = random.randint(1,64)
                    hep = CardMessage(
                        Card(
                            Module.Header('探索 | 下界'+name+'地区'),
                            Module.Divider(),
                            Module.Section("玩家"+user+"探索地狱堡垒"+Success+"\n获得了[下界犹*"+str(sl)),
                            Module.Divider(),
                            Module.Context(Element.Text("由 (met)237938831(met) 开发,  在 [Github](https://github.com/Buelie) 查看源码", type=Types.Text.KMD)),
                            color='#5A3BD7'
                        )
                    )
                    exp[user] += 5
        elif exp[user] < 50:
            hep = CardMessage(
                Card(
                    Module.Header('探索 | 下界'+name+'地区'),
                    Module.Divider(),
                    Module.Section("玩家"+user+"探索下界失败,原因:经验值不足(经验值>=50即可探索)"),
                    Module.Divider(),
                    Module.Context(Element.Text("由 (met)237938831(met) 开发,  在 [Github](https://github.com/Buelie) 查看源码", type=Types.Text.KMD)),
                    color='#5A3BD7'
                )
            )
    await msg.ctx.channel.send(hep)

# 抽奖系统

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
