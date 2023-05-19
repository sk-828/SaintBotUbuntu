import math
import discord
from discord.ext import tasks
from datetime import datetime
import random
import re
from dotenv import load_dotenv
import sqlite3
import datetime
import os
import json
import requests
import codecs
from func import download_image_class
#import requests

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

fileR1 = open('text/R1.txt', encoding="utf-8")
R1 = fileR1.readlines()
fileR2 = open('text/R2.txt', encoding="utf-8")
R2 = fileR2.readlines()
fileR3 = open('text/R3.txt', encoding="utf-8")
R3 = fileR3.readlines()
fileR4 = open('text/R4.txt', encoding="utf-8")
R4 = fileR4.readlines()
fileR5 = open('text/R5.txt', encoding="utf-8")
R5 = fileR5.readlines()
fileR5 = open('text/R5.txt', encoding="utf-8")
R5 = fileR5.readlines()
fileR1.close()
fileR2.close()
fileR3.close()
fileR4.close()
fileR5.close()
fileR18 = open('text/R18.txt', encoding="utf-8")
R18 = fileR18.readlines()
fileR18.close()
f = open('text/1.txt', encoding="utf-8")
contents = f.readlines()
f.close()
print(contents)
f = open('text/短距離.txt', encoding="utf-8")
short = f.readlines()
f.close()
f = open('text/マイル.txt', encoding="utf-8")
maile = f.readlines()
f.close()
f = open('text/中距離.txt', encoding="utf-8")
middle = f.readlines()
f.close()
f = open('text/長距離.txt', encoding="utf-8")
long = f.readlines()
f.close()
f = open('text/ダート.txt', encoding="utf-8")
dirt = f.readlines()
f.close()
f = open('text/エレイン.txt', encoding="utf-8")
elain = f.readlines()
f.close()
f = open('text/絵描きエレイン.txt', encoding="utf-8")
elain2 = f.readlines()
f.close()
f = open('text/全肯定リルシャロ.txt', encoding="utf-8")
charlotte = f.readlines()
f.close()
fileFR3 = open('text/FR3.txt', encoding="utf-8")
FR3 = fileFR3.readlines()
fileFR4 = open('text/FR4.txt', encoding="utf-8")
FR4 = fileFR4.readlines()
fileFR5 = open('text/FR5.txt', encoding="utf-8")
FR5 = fileFR5.readlines()

fileSR3 = open('text/SR3.txt', encoding="utf-8")
SR3 = fileSR3.readlines()
fileSR4 = open('text/SR4.txt', encoding="utf-8")
SR4 = fileSR4.readlines()
fileSR5 = open('text/SR5.txt', encoding="utf-8")
SR5 = fileSR5.readlines()

fileBR3 = open('text/BR3.txt', encoding="utf-8")
BR3 = fileBR3.readlines()
fileBR4 = open('text/BR4.txt', encoding="utf-8")
BR4 = fileBR4.readlines()
fileBR5 = open('text/BR5.txt', encoding="utf-8")
BR5 = fileBR5.readlines()

fileFR3.close()
fileFR4.close()
fileFR5.close()
fileSR3.close()
fileSR4.close()
fileSR5.close()
fileBR3.close()
fileBR4.close()
fileBR5.close()

#res = requests.get("https://script.google.com/macros/s/AKfycbyJLkB5dbYGurJsjbgJjJLJkKhh9rWp1I-dc-RVt47GexRtCIG3Y2iGgv2ncyREQCihXg/exec?row=10") 
#tarotComments=res.json()

pattern_dice = "[0-9]{1,2}D[0-9]{1,3}"
pattern_point = "[0-9]{1,8}"
split_pattern = 'D'

charas = {}

# with open('1.txt',encoding="utf-8") as f:
#  contents = f.read()
#  print(contents
# )

def search(name,guildid):
    con=sqlite3.connect("charaDB.db")
    result = con.execute("SELECT * FROM chara where name=? and guildID=?;",(name,guildid))
    for row in result:
        return row
    return 0
def searchLike(name,guildid):
    con=sqlite3.connect("charaDB.db")
    result = con.execute("SELECT * FROM chara where name like ? and guildID=?;",("%"+name+"%",guildid))
    return result

def searchDelete(name,guildid,authorid):
    con=sqlite3.connect("charaDB.db")
    try:
       con.execute("DELETE FROM chara where name=? and guildID=? and autorID=? ;",(name,guildid,authorid))
    except sqlite3.IntegrityError:
        con.rollback()
    finally:
        con.commit()

def task():
    for i in range(0,12):
        url ="https://script.google.com/macros/s/AKfycbyJLkB5dbYGurJsjbgJjJLJkKhh9rWp1I-dc-RVt47GexRtCIG3Y2iGgv2ncyREQCihXg/exec?row=" + str(i)
        filename = str(i) +".json"
        urlData = requests.get(url).content
        with open(filename ,mode='wb') as f: # wb でバイト型を書き込める
            f.write(urlData)
    makeDB()

def makeDB():
    global charas
    charas ={}
    for i in range(1,7):
        filename = str(i) +".json"
        f = open(filename, encoding="utf-8")
        a = f.readlines()
        f.close()
        a=a[0].strip('[["')
        a=a.strip('"]]')
        a=a.split('"],["')
        b=[]
        for i in a:
            b.append(i.split('","'))
        for i in range(1,len(b)-1):
            charas[b[i][0]]="一人称:"+b[i][4]+", 二人称:"+b[i][5]
    print("OK")


@client.event
async def on_ready():
    loop.start()
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@tasks.loop(hours=24)
async def loop():
    task()

@client.event
async def on_message(message):
    if message.content.startswith("/update"):
        task()
    if message.content.startswith("/chara"):
        msg=message.content.split()
        print(charas)
        if msg[1] in charas:
            me=charas[msg[1]]
            await message.channel.send(msg[1]+"   "+me)
    if message.content.startswith("/pokeS"):
        msg=message.content.split(" ")
        n=int(msg[1])+20
        junsoku=int(msg[1])+52
        saisoku=round((int(msg[1])+52)*1.1,1)
        await message.channel.send("無振り:"+str(n)+" 準速:"+str(junsoku)+" 最速"+str(saisoku)+" 最速スカーフ"+str(round(saisoku*1.5)))
    if message.content.startswith("/pokeRS"):
        msg=message.content.split(" ")
        speed=int(msg[1])
        n=int(msg[1])-20
        junsoku=int(msg[1])-52
        saisoku=round((int(msg[1])/1.1-52),1)
        await message.channel.send("無振り:"+str(n)+"抜き 準速:"+str(junsoku)+"抜き 最速"+str(saisoku)+"抜き")
    if message.content.startswith("/delill "):
        msg=message.content.split(" ")
        searchDelete(msg[1],message.guild.id,message.author.id)
    if message.content.startswith("/delill　"):
        msg=message.content.split("　")
        searchDelete(msg[1],message.guild.id,message.author.id)
    if message.content.startswith("/serill "):
        msg=message.content.split(" ")
        print(msg[1])
        result=searchLike(msg[1],message.guild.id)
        if result!=0:
            for row in result:
                await message.channel.send(row[0])
    if message.content.startswith("/serill　"):
        msg=message.content.split("　")
        print(msg[1])
        result=searchLike(msg[1],message.guild.id)
        if result!=0:
            for row in result:
                await message.channel.send(row[0])
    if message.content.startswith("/ill "):
        msg=message.content.split(" ")
        print(msg[1])
        result=search(msg[1],message.guild.id)
        if result!=0:
          filepass=result[3]
          await message.channel.send(file=discord.File(filepass))
    if message.content.startswith("/ill　"):
        msg=message.content.split("　")
        result=search(msg[1],message.guild.id)
        if result!=0:
          filepass=result[3]
          await message.channel.send(file=discord.File(filepass))
    if message.content.startswith("/addill "):
        msg=message.content.split(" ")
        result=search(msg[1],message.guild.id)
        if result==0:
            date = datetime.datetime.now()
            con=sqlite3.connect("charaDB.db")
            filepass="img/"+date.strftime("%Y%m%d%H%M%S") + ".png"
            try:
                con.execute("INSERT INTO chara VALUES (?, ?, ? ,?)",(msg[1],message.guild.id,message.author.id,filepass))
            except sqlite3.IntegrityError:
                con.rollback()
            finally:
                con.commit()
                download_image_class(message,filepass)
        else:
            await message.channel.send("その名前は既に登録されています。")
    if message.content.startswith("/addill　"):
        msg=message.content.split("　")
        result=search(msg[1],message.guild.id)
        if result==0:
            date = datetime.datetime.now()
            con=sqlite3.connect("charaDB.db")
            filepass="img/"+date.strftime("%Y%m%d%H%M%S") + ".png"
            try:
                con.execute("INSERT INTO chara VALUES (?, ?, ? ,?)",(msg[1],message.guild.id,message.author.id,filepass))
            except sqlite3.IntegrityError:
                con.rollback()
            finally:
                con.commit()
                download_image_class(message,filepass)
        else:
            await message.channel.send("その名前は既に登録されています。")

    if message.content.startswith("/タロット"):
        array=[0]*22
        for i in range(22):
            array[i]=i
        random.shuffle(array)
        temp=random.random()
        if temp < 0.5:
            filepass="img/tarot/"+str(array[0])+".jpg"
            #m=tarotComments[array[0]+1][1]+"の正位置:"+tarotComments[array[0]+1][2]
        else:
            filepass="img/tarotR/"+str(array[0])+".jpg"
            #m=tarotComments[array[0]+1][1]+"の逆位置:"+tarotComments[array[0]+1][3]
        await message.channel.send(file=discord.File(filepass))
        #await message.channel.send(m)
        temp2=random.random()
        if temp2 < 0.5:
            filepass="img/tarot/"+str(array[7])+".jpg"
            #m=tarotComments[array[7]+1][1]+"の正位置:"+tarotComments[array[7]+1][2]
        else:
            filepass="img/tarotR/"+str(array[7])+".jpg"
            #m=tarotComments[array[7]+1][1]+"の逆位置:"+tarotComments[array[7]][3]
        await message.channel.send(file=discord.File(filepass))
        #await message.channel.send(m)
    if message.content.startswith("/レース"):
        if client.user != message.author:
            s = random.randint(0, len(short) - 1)
            m = random.randint(0, len(maile) - 1)
            mi = random.randint(0, len(middle) - 1)
            l = random.randint(0, len(long) - 1)
            d = random.randint(0, len(dirt) - 1)
            await message.channel.send(short[s]+maile[m]+middle[mi]+long[l]+dirt[d])
    if message.content.startswith("/短距離"):
        if client.user != message.author:
            s = random.randint(0, len(short) - 1)
            await message.channel.send(short[s])
    if message.content.startswith("/マイル"):
        if client.user != message.author:
            s = random.randint(0, len(maile) - 1)
            await message.channel.send(maile[s])
    if message.content.startswith("/中距離"):
        if client.user != message.author:
            s = random.randint(0, len(middle) - 1)
            await message.channel.send(middle[s])
    if message.content.startswith("/長距離"):
        if client.user != message.author:
            s = random.randint(0, len(long) - 1)
            await message.channel.send(long[s])
    if message.content.startswith("/ダート"):
        if client.user != message.author:
            s = random.randint(0, len(dirt) - 1)
            await message.channel.send(dirt[s])
    if message.content.startswith("/エレイン"):
        if client.user != message.author:
            s = random.randint(0, len(elain) - 1)
            await message.channel.send(elain[s])
    if message.content.startswith("/絵描きエレイン"):
        if client.user != message.author:
            s = random.randint(0, len(elain2) - 1)
            await message.channel.send(elain2[s])
    if message.content.startswith("/全肯定"):
        if client.user != message.author:
            s = random.randint(0, len(charlotte) - 1)
            await message.channel.send(charlotte[s])
    if message.content.startswith("カイくん"):
        if client.user != message.author:
            await message.channel.send("好きなのかい？")
    # 「おはよう」で始まるか調べる
    if message.content.startswith("/swp"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            msg=message.content
            result = re.search(pattern_point, msg)
            if result:
                p=int(result.group())
                if p<7000:
                    m=math.floor(p/1000)
                elif p<16000:
                    m=math.floor((p-6000)/1500+6)
                elif p<104500:
                    m=math.floor((p-14500)/2000+12)
                else:
                    m=math.floor((p-102500)/2500+56)
                await message.channel.send("現在の経験点"+result.group()+"点だと"+str(m)+"回まで成長できます")

    #if message.content.startswith("/d"):
    #    msg=message.content
    #    result=re.search(pattern_dice,msg)
    if message.content.startswith("/お題"):
        if client.user != message.author:
            s = random.randint(0, len(contents) - 1)
            await message.channel.send(contents[s])
    if message.content.startswith("/ガチャ"):
        if client.user != message.author:
            gacha = random.randint(0, 100)
            if gacha <= 79:
                s = random.randint(0, len(R3) - 1)
                await message.channel.send("★★★" + R3[s])
            elif gacha <= 97:
                s = random.randint(0, len(R4) - 1)
                await message.channel.send("★★★★" + R4[s])
            elif gacha <= 100:
                s = random.randint(0, len(R5) - 1)
                await message.channel.send("★★★★★" + R5[s])
    if message.content.startswith("/10連ガチャ"):
        if client.user != message.author:
            for i in range(9):
                gacha = random.randint(1, 100)
                if gacha <= 79:
                    s = random.randint(0, len(R3) - 1)
                    await message.channel.send("★★★" + R3[s])
                elif gacha <= 97:
                    s = random.randint(0, len(R4) - 1)
                    await message.channel.send("★★★★" + R4[s])
                elif gacha <= 100:
                    s = random.randint(0, len(R5) - 1)
                    await message.channel.send("★★★★★" + R5[s])
            gacha = random.randint(0, 100)
            if gacha <= 97:
                s = random.randint(0, len(R4) - 1)
                await message.channel.send("★★★★" + R4[s])
            elif gacha <= 100:
                s = random.randint(0, len(R5) - 1)
                await message.channel.send("★★★★★" + R5[s])
    if message.content.startswith("/SW福袋"):
        if client.user != message.author:
            for i in range(9):
                gacha = random.randint(1, 100)
                if gacha <= 79:
                    s = random.randint(0, len(R3) - 1)
                    await message.channel.send("★★★" + R3[s])
                elif gacha <= 97:
                    s = random.randint(0, len(R4) - 1)
                    await message.channel.send("★★★★" + R4[s])
                elif gacha <= 100:
                    s = random.randint(0, len(R5) - 1)
                    await message.channel.send("★★★★★" + R5[s])
            s = random.randint(0, len(R5) - 1)
            await message.channel.send("★★★★★" + R5[s])
    if message.content.startswith("/Rお題"):
        if client.user != message.author:
            s = random.randint(0, len(R18) - 1)
            await message.channel.send(R18[s])
    if message.content.startswith("/KBF"):
        dice=random.randint(1,101)
        if dice>=96:
            await message.channel.send("☆☆☆☆☆ "+random.choice(FR5))

        elif dice>=70:
            await message.channel.send("☆☆☆☆ "+random.choice(FR4))
        else:
            await message.channel.send("☆☆☆ "+random.choice(FR3))
    if message.content.startswith("/KBS"):
        dice=random.randint(1,101)
        if dice>=96:
            await message.channel.send("☆☆☆☆☆ "+random.choice(SR5))
        elif dice>=70:
            await message.channel.send("☆☆☆☆ "+random.choice(SR4))
        else:
            await message.channel.send("☆☆☆ "+random.choice(SR3))
    if message.content.startswith("/KBB"):
        dice=random.randint(1,101)
        if dice>=96:
            await message.channel.send("☆☆☆☆☆ "+random.choice(BR5))
        elif dice>=70:
            await message.channel.send("☆☆☆☆ "+random.choice(BR4))
        else:
            await message.channel.send("☆☆☆ "+random.choice(BR3))
                

load_dotenv()
client.run(os.getenv("DISCORD_TOKEN"))