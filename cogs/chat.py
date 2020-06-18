import discord
from discord.ext import commands
from discord.utils import get

import random
import json
from os import system

class chat(commands.Cog):


    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['delete', 'purge'], brief='!apagar [x]', description='Deleta as [x] mensages anteriores')
    async def clear(self, ctx, limit):
        try:
            float(limit)
        except:
            await ctx.send('❌ insira um inteiro !')
        else:
            if str(ctx.channel) == 'estudos':
                limit = int(limit) + 1
                await ctx.channel.purge(limit=limit)
            else:
                await ctx.send('❌ Wrong channel ! Must be used in "commands" channel !')

    @commands.command(name="fome",
                    aliases=["Fome", "FOME"],
                    description="Fome",
                    brief="Fome")
    async def fome(self, ctx):
        words = ctx.message.content.split(" ")
        possible_responses = [
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
        if "ome" in words[0].lower():
            r = random.choice(possible_responses)
            await ctx.send(r, tts=False)

    ##########

    @commands.command(name="carlinhos",
                    aliases=["Carlinhos", "CARLINHOS"],
                    description="Carlinhos",
                    brief="Carlinhos")
    async def carlinhos(self, ctx):
        await ctx.send(file=discord.File('0.jpg'), tts=False)

    ##########

    @commands.command(name="controle",
                    aliases=["Controle", "CONTROLE"],
                    description="controle",
                    brief="controle")
    async def controle(self, ctx):
        await ctx.send("não esquece de me devolver essa porra", tts=True)
        await asyncio.sleep(10)
        await ctx.send("e não pode por menos de 20 graus heim caralho", tts=True)

    ###########

    @commands.command(name="chave",
                    aliases=["Chave", "CHAVE"],
                    description="chave",
                    brief="Chave")
    async def controle(self, ctx):
        await ctx.send("vocês estão em 3?", tts=True)
        await asyncio.sleep(10)
        await ctx.send("devolver daqui quatro horas", tts=True)
        await asyncio.sleep(14400)
        await ctx.send("ta na hr de renovar essa porra seus vagabundos", tts=True)

    ##########

    @commands.command(name="cafe",
                    aliases=["Cafe", "CAFE", "coffee", "café", "Café"],
                    description="café",
                    brief="café")
    async def cafe(self, ctx):
        await ctx.send(file=discord.File('1.jpg'), tts=False)

    ##########

    @commands.command(name="corte",
                    aliases=["Corte", "CORTE"],
                    description="corte",
                    brief="corte")
    async def corte(self, ctx):
        await ctx.send(file=discord.File('2.jpg'), tts=False)

    ##########

    @commands.command(name="mari",
                    aliases=["famosa", "a famosa", "Mari"],
                    description="mari",
                    brief="mari")
    async def mari(self, ctx):
        await ctx.send(file=discord.File('3.jpg'), tts=False)

    ##########

    @commands.command(name="ju",
                    aliases=["turista", "Ju", "brisa"],
                    description="ju",
                    brief="ju")
    async def ju(self, ctx):
        await ctx.send(file=discord.File('4.jpg'), tts=False)

    ##########

    @commands.command(name="jeffao",
                    aliases=["jeff", "jefao", "jefão"],
                    description="jefao",
                    brief="jefao")
    async def jeffao(self, ctx):
        tr = (random.randint(5, 7))
        await ctx.send(file=discord.File("{}.jpg".format(tr)), tts=False)



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
    # @commands.command(brief='!help [category/none]', description="Displays an help message")
    # async def help(self, ctx, *c):
    #     if not c:
    #         await ctx.channel.purge(limit=1)
    #         temp = []
    #         embed = discord.Embed(color=discord.Color.blue(), title='commands list :')
    #         for x in self.bot.cogs:
    #             for y in self.bot.get_cog(x).get_commands():
    #                 if not y.hidden:
    #                     temp.append(f"\n{y.brief}")
    #             embed.add_field(name=f'**{x} :**', value=f"{''.join(temp[0:len(temp)])}", inline=False)
    #             temp = []
    #         await ctx.send(embed=embed)
    #     elif len(c) == 1:
    #         c = ''.join(c[:])
    #         if self.bot.get_cog(c):
    #             await ctx.channel.purge(limit=1)
    #             embed = discord.Embed(color=discord.Color.blue(), title=f'bot in "{c}" category')
    #             for x in self.bot.get_cog(c).get_commands():
    #                 if not x.hidden:
    #                     embed.add_field(name=f'**{x.brief} :**', value=f"{x.description}", inline=False)
    #             await ctx.send(embed=embed)
    #         else:
    #             await ctx.send("❌ Category name wasn't found !")
    #     else:
    #         await ctx.send("❌ You have to input only one category !")


def setup(bot):
    bot.add_cog(chat(bot))
