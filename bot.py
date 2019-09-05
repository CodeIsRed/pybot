import discord,os
import asyncio


client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('!hi'):
        ch = message.channel
        user = message.author
        msg = 'Hello {0.author.mention} {}'.format(message,user.id)
        await ch.send(msg)
@client.event
async def on_ready():
    game = discord.Activity(name="Beta MrEinstien Network", type=discord.ActivityType.listening)
    await client.change_presence(status=discord.Status.dnd, activity=game)
    


client.run(os.getenv('token'))
