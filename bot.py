import discord,os
import asyncio


client = discord.Client()
TOKEN = os.environ['token']

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!hi'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        
@client.event
async def on_ready():
    print('Login as ')
    print(client.user.name)
    print(client.user.id)
    print('-----')


client.run(TOKEN)

        
