import discord
from discord import app_commands
import os

TOKEN = os.getenv("TOKEN")

# Prueba temporal para Render
print("TOKEN CARGADO:", TOKEN[:10] if TOKEN else "NO HAY TOKEN")


class MyBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True

        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()


bot = MyBot()


@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}")


# /ping
@bot.tree.command(name="ping", description="Responde con pong")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("pong🏓")


@bot.event
async def on_message(message):

    if message.author.bot:
        return

    texto = message.content.lower()


    # weko! @usuario
    if texto.startswith("weko!"):
        if message.mentions:
            usuario = message.mentions[0]
            await message.channel.send(
                f"Muy wekereque de tu parte {usuario.mention} 👀👀👀"
            )
            return


    # puto
    if "puto" in texto:
        await message.channel.send("eres vos")
        return


    # que
    if texto.strip() == "que":
        await message.channel.send("so")
        return


    # queque / advincula
    if "queque" in texto or "advincula" in texto or "luis advincula" in texto:
        await message.channel.send("quiero queque")
        await message.channel.send(
            "https://i.pinimg.com/originals/9d/50/3b/9d503bd66edbe040e00220836a2a4256.jpg"
        )
        return


    # xala
    if "xala" in texto:
        await message.channel.send("callate malaya ctm")
        return


    # malaya
    if "malaya" in texto:
        await message.channel.send("calla perro ctm")
        return


    # che / boludo
    if "che" in texto or "che boludo" in texto or "boludo" in texto:
        await message.channel.send(
            "https://images8.alphacoders.com/530/530088.jpg"
        )
        return


    # jueves
    if "jueves" in texto:
        await message.channel.send(
            "https://i.pinimg.com/736x/6d/c6/11/6dc611982acccab162c4cf947c645399.jpg"
        )
        return


    # fracasado
    if "fracasado" in texto:
        await message.channel.send(
            "eres por tratar de papear a otra gente"
        )
        return


    await bot.process_commands(message)


bot.run(TOKEN)
