import discord
from discord.ext import commands
from discord.utils import get

import random
import json
from os import system

class chat(commands.Cog):


    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['delete'], brief='!apagar [x]', description='Deleta as [x] mensages anteriores')
    async def clear(self, ctx, limit):
        try:
            float(limit)
        except:
            await ctx.send('❌ insira um inteiro !')
        else:
            if str(ctx.channel) == 'comandos':
                limit = int(limit) + 1
                await ctx.channel.purge(limit=limit)
            else:
                await ctx.send('❌ Canal errado, use no canal "comandos" !')

    # Como declarar um comando que retorna uma mensagem de texto
    # @commands.command(name="nome_do_comando",
    #                 aliases=["outra forma de chamalo"],
    #                 description="descricao",
    #                 brief="breve descricao")
    #async def nome_do_comando(self, ctx):
    #   (bloco do codigo)
    #await ctx.send('saida de texto', tts=False)

    #exemplo de um comando para retornar uma mensagem de texto
    """
    @commands.command(name="fome",
                    aliases=["Fome", "FOME"],
                    description="Fome",
                    brief="Fome")
    async def fome(self, ctx):
        respostas_possiveis = [
            "Come uma laranja",
            "Come uma banana",
            "Come o cu de quem ta lendo",
            "Come uma pizza",
            "Come um lanchão",
            "Come uma marmitop",
            "Come pão com linguiça",
            "Come nuggets",
            "Come batata frita",
            "Come costelinha assada",
            "Come cebola empanada",
            "Come torresmo",
            "Come pastel",
            "Come paçoca",
            "Come coxinha",
            "Come pão com mortadela",
        ]
        resposta = random.choice(respostas_possiveis)
        await ctx.send(resposta, tts=False)
    """
    ##########

    # Como declarar um comando que retorna imagem na mensagem
    # @commands.command(name="nome_do_comando",
    #                 aliases=["outra forma de chamalo"],
    #                 description="descricao",
    #                 brief="breve descricao")
    #async def nome_do_comando(self, ctx):
    #   (bloco do codigo)
    #await ctx.send(file=discord.File('fotos/0.jpg'), tts=False)

    #exemplo de um comando para retornar uma imagem
    """
    @commands.command(name="nome_de_um_usuario",
                    aliases=["apelido"],
                    description="foto de (nome do usuario)",
                    brief="foto do (nome do usuario)")
    async def nome_de_um_usuario(self, ctx):
        await ctx.send(file=discord.File('fotos/{nomedoarquivo.jpg}'), tts=False)

    ##########

    #exemplo de um comando para retornar uma imagem de um conjunto de imagens
    @commands.command(name="nome_do_comando",
                    aliases=[],
                    description="comando",
                    brief="comando")
    async def nome_do_comando(self, ctx):
        nome_das_fotos = [
            "foto1.jpg",
            "foto2.jpg",
            "foto_n.jpg"
        ]
        nome_da_foto = random.choice(nome_das_fotos)
        await ctx.send(file=discord.File(nome_da_foto), tts=False)
    """
    ##########
    """
    @commands.command(name="pa",
                    aliases=["to pa", "TO PA", "To Pa"],
                    description="ficou pa",
                    brief="pistolou")
    async def pa(self, ctx):
        autor = ctx.message.author
        a_file = open("data.json", "r")
        json_object = json.load(a_file)
        a_file.close()
        if json_object.get(autor.name) != None:
            json_object[autor.name] += 1
            Pa = json_object[autor.name]
            a_file = open("data.json", "w")
            json.dump(json_object, a_file)
            a_file.close()
            await ctx.send(f"{autor.name} ficou pa pela {Pa} vez")
        else:
            json_object.update({autor.name : 1})
            a_file = open("data.json", "w")
            json.dump(json_object, a_file)
            a_file.close()
            await ctx.send(f"{autor.name} ficou pa pela primeira vez")
    """
def setup(bot):
    bot.add_cog(chat(bot))
