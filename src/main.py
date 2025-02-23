import discord
import asyncio
import aiohttp
import os
import sys
from discord.ext import commands
from dotenv import load_dotenv

# Charger les variables d'environnement du fichier .env
load_dotenv()

TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise ValueError("[-] ERREUR : Le TOKEN n'a pas été chargé depuis .env !")
print(f"[+] TOKEN chargé : {TOKEN[:5]}...")

bot = commands.Bot(command_prefix='?', intents=discord.Intents.all())
tree = bot.tree

async def main():
    print(("[+] Lancement du bot"))

    # Toutes les fonctions (event)
    for file in os.listdir("cogs"):
        if file.endswith(".py") and not file.startswith("_"):
            await bot.load_extension(f"cogs.event.{file[:-3]}")
    
    # Toutes les fonctions (commandes)
    for file in os.listdir("cogs"):
        if file.endswith(".py") and not file.startswith("_"):
            await bot.load_extension(f"cogs.commands.{file[:-3]}")

    await bot.start(TOKEN)

try :
    asyncio.run(main())
except discord.errors.LoginFailure:
    print("[-] Echec de la connexion (souvent du à un token invalide)")
except KeyboardInterrupt:
    print("[-] Arrêt du bot")
except Exception as e:
    print(f"Erreur non prise en charge par le système : {e}")