import discord
import random
import asyncio
import os

from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = '.')

# Status cycle set
status = cycle(['Anything you want!',
                'Random status number #2'])

# Initializing bot's extensions
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# Bot is ready event!
@client.event
async def on_ready():
    await client.change_presence(activity = discord.Game('Starting bot up!'))
    status_update.start()
    print("Bot is Online!")

# If an error occurs, send that error as a discord message on the user active channel
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please use required arguments.')
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send('User lacks permission to use that command.')
    else:
        await ctx.send(f'Erro: {error}')

# Update status every x seconds
@tasks.loop(seconds = 60)
async def status_update():
    await client.change_presence(activity = discord.Game(next(status)))

@client.command(brief='Kick a specific member.', description='This command will kick a specific member. Use: .kick @member')
@commands.has_permissions(administrator = True, manage_messages = True, manage_roles = True)
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)
    await ctx.send(f"Kickando {user.mention}!")



@client.command(brief='Clear x messages from chat', description='This command will clear x messages from chat. (Max 20 messages) Use: .clear (number of messages *default clear = 2*)')
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount = 2):
    # Clears "amount" messages from the chat. Default is "command + 2" messages.
    #   --> No deleting messages older than "x" days. (default might be anytime);
    #       Delete all messages from a specific user or from a specific user since "x" days ago;

    async def DeleteALL(amount):
        await ctx.channel.purge(limit=(amount + 1))
        await ctx.channel.send(f'Cleared {amount} messages. 👍')

    if (amount > 20):
        amount = 20

    if (amount >= 10):
        await ctx.send(f"Are you sure? (Y)")

        def checkClear(response):
            if response.content == "Y":
                return True
        try:
            await client.wait_for('message', timeout=10.0, check=checkClear)
        except asyncio.TimeoutError:
            await ctx.send("Clear failed. No response given.")
        else:
            await DeleteALL(amount)
    else:
        await DeleteALL(amount)

#############################################################################################################################################

# Load, unload and reload (all or one) extensions
@client.command(brief='Load a specific extension', description='Bot will load a specific extension. Use: .load (name of the extension)')
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Loaded extension [{extension}]!')

@client.command(brief='Unload a specific extension', description='Bot will unload a specific extension. Use: .unload (name of the extension)')
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Unloaded extension [{extension}]!')

@client.command(brief='Reload a specific extension', description='Bot will reload a specific extension. Use: .reload (name of the extension)')
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Reloaded extension [{extension}]!')

@client.command(brief='Bot will reload all extensions', description='Bot will reload all extensions. Use: .reloadall')
async def reloadall(ctx):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.unload_extension(f'cogs.{filename[:-3]}')
            client.load_extension(f'cogs.{filename[:-3]}')
    await ctx.send(f'Reloaded extensions!')

# Open token file, read it and use it to run the client. Stored outside code for safekeeping.
fileOpen = os.open("C:\\Users\\AlwaysLWIN\\Documents\\AlwaysDiscordBOT\\Token.txt", os.O_RDONLY)
token = os.read(fileOpen, 59)
os.close(fileOpen)
tokenNew = str(token).split('\'')[1]
client.run(f'{tokenNew}')
