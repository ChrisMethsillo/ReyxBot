import discord
import json
import os
import random 
import datetime

from mcrcon import MCRcon

client = discord.Client()

#Execute a command on the minecraft server
def executeCommand(cmd):
    with MCRcon(os.getenv("IPADDRESS"), os.getenv("PASSWORD")) as mcr:
        return mcr.command(cmd)

#Returns a message of how much time is left to be able to execute a certain action
def checkTime(user):
    hoy =datetime.datetime.now()
    f = open("userTimes.json")
    file = json.load(f)

    for i in file:
        if i["usuario"] == user:
            tiempoRestante = (datetime.datetime.strptime(i["fecha"], "%Y-%m-%d %H:%M:%S.%f") + datetime.timedelta(days=1) - hoy).total_seconds()
            return "Te quedan: " + str(int(tiempoRestante/3600)) + " horas y " + str(int(tiempoRestante%3600/60)) + " minutos"
    
   
#Check if a player is online or not on the minecraft server
def checkPlayer(user):
    online = executeCommand("list")
    players = online.split(":")[1]
    players = players.replace(" ", "")
    players = players.split(",")
    return user in players

def chechLastExec(user):
    hoy = datetime.datetime.now()
    f = open("fechas.json")
    file = json.load(f)

    for i in file:
        if i["usuario"] == user:
            if (hoy - datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S.%f") >= i["fecha"]:
                i["fecha"] = hoy.strftime("%Y-%m-%d %H:%M:%S.%f")
                with open("fechas.json", "w") as f:
                    json.dump(file, f)
                return True
            else:
                return False
                 
    
    day = hoy.strftime("%Y-%m-%d %H:%M:%S.%f")
    newUser = {
        "usuario" : user,
        "fecha" : day
    }
    file.append(newUser)
    with open("fechas.json", "w") as f:
        json.dump(file, f)
    return True
   

#Give money in the minecraft server to a player

def giveMoney(user, amount):
    executeCommand("give " +user+ " iron_nugget{Unbreakable:1,display:{Name:'[{\"text\":\"Chaucha\",\"italic\":false,\"color\":\"aqua\"}]'},Enchantments:[{id:unbreaking,lvl:3}]} " + str(amount))
    

#Simple model what simulates a roullete game
def ruleta(message, persona):
    emojis = [":poop:",":nauseated_face:",":sob:",":clown:"  ,":grin:",":flushed:" ,":star_struck:" ,":money_mouth:"]
    result = [random.randint(0,7) for i in range(3)]
    ruleta = "**Ruleta:** " + emojis[result[0]] + " " + emojis[result[1]] + " " + emojis[result[2]]

    for i in set(result):
        if result.count(i) == 2:
            if i == 0:
                executeCommand("kill "+ persona)
                return ruleta + " \n\nTE GANASTE UNA SACA DE CHUCHA :smiling_imp: "
            if i == 4:
                giveMoney(persona, 1)
                return ruleta + "\n\nTe ganaste 1 chaucha :money_mouth:"
            if i == 5:
                giveMoney(persona, 10)
                return ruleta +"\n\nTe ganaste 10 chauchas :money_mouth:" 
            if i == 6:
                giveMoney(persona, 15)
                return ruleta +"\n\nTe ganaste 15 chauchas :money_mouth:"

        if result.count(i) == 3:
            if i == 0:
                executeCommand("kill "+ persona)
                return ruleta + " \n\nTE GANASTE UNA SACA DE CHUCHA :smiling_imp: "
            if i == 4:
                giveMoney(persona, 2)
                return ruleta + "\n\nTe ganaste 2 chauchas :money_mouth:"
            if i == 5:
                giveMoney(persona, 20)
                return ruleta +"\n\nTe ganaste 20 chauchas :money_mouth:" 
            if i == 6:
                giveMoney(persona, 25)
                return ruleta +"\n\nTe ganaste 25 chauchas :money_mouth:"
            if i == 7:
                giveMoney(persona, 64)
                return ruleta +"\n\nTe ganaste 64 chauchas :money_mouth:"
            
                

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$cmd'):
        userRoles= [role.name for role in message.author.roles]
        if "Minecraft Admins" in userRoles:
            try :
                cmd = message.content.replace("$cmd ", "")
                executeCommand(cmd)
                await message.channel.send("Ok admin " + message.author.mention + " :money_mouth:")
            except:
                await message.channel.send("No se pudo ejecutar el comando")
        else:
            await message.channel.send("No eres admin (:money_mouth:) pa ejecutar esto ") 
    
    if message.content.startswith('$whitelist'):
        name = message.content.replace("$whitelist ", "")
        try:
            executeCommand("whitelist add " + name)
            await message.channel.send("Se añadio a la whitelist el usuario " + name + " :money_mouth:")
        except:
            await message.channel.send("No se pudo añadir al usuario a la whitelist ")

    if message.content.startswith('$online'):
        try:
            online = executeCommand("list")
            players = online.split(":")[1]
            players = players.replace(",","\n")
            await message.channel.send("Usuarios online :green_circle: : \n" + "```\n" + players + "\n```")
        except:
            await message.channel.send("No se pudo obtener la lista de usuarios online ")
    

    if message.content.startswith('$ruleta'):
        persona = message.content.replace("$ruleta ", "")

        if persona == "":
            await message.channel.send("No indicaste un nombre de usuario")
            return 
            
        if not checkPlayer(persona):
            await message.channel.send("El usuario " + persona + " no esta online")
            return 

        if not chechLastExec(persona):
            await message.channel.send("No puedes jugar la ruleta en menos de 24 horas :money_mouth:")
            await message.channel.send(checkTime(persona))

            return
        
        await message.channel.send(ruleta( persona))
        
          
client.run(os.getenv("TOKEN"))