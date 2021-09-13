import discord
import random
from discord.ext import commands

    # Example of Cog. Just a vanilla cog without real purpose.

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Exemple.py loaded!')

    @commands.command(brief='Ping the server.', description='This command will ping the server and return the ms.')
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.client.latency * 1000)}ms")


    # 8ball. You ask a question and it shall reply. Portuguese version.
    #   (mixed responses, positive or negative questions not balanced)

    @commands.command(aliases = ['8ball', 'pergunta', '?'], brief='Ask a question.', description='Ask a question and the bot will answer. Use: .? (Question)')
    async def _8ball(self, ctx, *, question):
        responses = ['Até onde eu vi, sim.',
                     'Pergunta depois.',
                     'Vo vê e te conto.',
                     'Tá dificil prever isso.',
                     'Se concentra e pergunta de novo.',
                     'Se eu fosse você, não esperaria por isso.',
                     'Mais certo do que 2 + 2 = 4.',
                     'Difinitivamente, sim.',
                     'Mais errado que 2 + 2 = 5.',
                     'Definitivamente, não.',
                     'Olha... Não.',
                     'Nem fodendo.',
                     'Fodendo sim.',
                     'Cê quem sabe.',
                     'Até onde eu vejo, acho que sim.',
                     'Mais duvidoso do que produto do paraguai na 25 de março.',
                     'Sem sombra de dúvidas.',
                     'Sim.',
                     'Não.',
                     'Dá pra confiar que sim.']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

def setup(client):
    client.add_cog(Example(client))