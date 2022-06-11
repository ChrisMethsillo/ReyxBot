# ReyxBot, The best minecraft admin bot
Este es un bot de discord que interactua con un servidor personalizado de minecraft en el cual juego con amigos
La gracia de este bot es que añade distintas interacciones entre los usuarios de discord y un servidor de minecraft,
anadiendo distintas mecanicas como una ruleta aleatoria que dropea items en el juego, entregar una lista de los
jugadores conectados al servidor de minecraft, permite ejecutar comandos en la consola a traves de mensajes en 
discord, etc.

## Requerimientos

- [Python 3.9](https://www.python.org/)
- [MCRcon](https://pypi.org/project/mcrcon/)
- [Discord API wrapper](https://discordpy.readthedocs.io/en/stable/)   

## Como se instala?

Primero que todo, debes tener habilitado el [portal de desarrollo de discord](https://discord.com/developers/applications) y añadir este bot dentro de tus aplicaciones con los siguientes permisos:
- Read Messages/View Channels
- Send Messages
- Manage Messages

Luego de esto, en tu servidor de minecraft debes tener habilitado tu protocolo [RCON](https://wiki.vg/RCON) el cual te permite ejecutar comandos en tu servidor de minecraft de manera remota.

Ya con estos dos pasos realizados, creas un archivo de ambiente .env en donde tendras tu token de discord, tu ip y password de servidor, definidos de la siguiente manera:
- token: TOKEN
- ip del servidor: IPADDRESS
- password del servidor : PASSWORD 

Ya con esto realizado, solo queda ponerlo en ejecucion (basta con ejecutar ```python Reyxbot.py ```) e invitarlo a tu servidor de discord

## Comandos dentro de tu servidor
Como gran parte de los bots de discord, se utiliza un prefijo (en este caso ``` $```) para indicar la ejecucion de un comando en el bot.

- ```$cmd "comando de minecraft"```: Ejecuta un comando de minecraft en tu servidor.
- ```$whitelist username```: Añade a un usuario a la whitelist del servidor de minecraft.
- ```$online"```: Entrega la lista de usuarios conectados al servidor de minecraft.

- ```$ruleta username"```: Esto es un minijuego que representa una ruleta, dependiendo el resultado, este entrega items al usuario dentro del servidor.

Algunos de estos comandos requieren de un rol especial para poder ejecutarlos, esto se puede modificar dentro del codigo.

## Por que se llama Reyxbot?
Esto dado a la persona que le puso mas cariño a nuestro servidor, haciendo que dentro de este hayan mas mecanicas aparte de las ya entregadas por el mismo juego, desde economia, mazmorras, e incluso historia relacionada al juego.

 
