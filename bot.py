import discord,os
import asyncio


client = discord.Client()
client = commands.Bot(command_prefix = '?')

@client.command()
async def hey(ctx):
    await client.send('hi')
        
@client.event
async def on_ready():
    game = discord.Activity(name="Beta MrEinstien Network", type=discord.ActivityType.listening)
    await client.change_presence(status=discord.Status.dnd, activity=game)
    


client.run(os.getenv('token'))
        
