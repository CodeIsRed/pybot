import discord,os
import asyncio


client = discord.Client()


@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    if message.content.startswith('!hi'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        
@client.event
async def on_ready():
    game = discord.Activity(name="Beta MrEinstien Network", type=discord.ActivityType.listening)
    await client.change_presence(status=discord.Status.dnd, activity=game)
    print('Login as ')
    print(client.user.name)
    print(client.user.id)
    print('-----')


client.run(os.getenv('token'))
        
