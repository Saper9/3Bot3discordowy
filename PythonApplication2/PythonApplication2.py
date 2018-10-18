import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get
import asyncio
import time

Client=discord.Client()
client=commands.Bot(command_prefix='%') #chuj wie po co
#zmienne
tabcom=["%napierdolony","%au","%test","%tfar","%acre","%mechy","%czapka"]
tabcomlen=len(tabcom)

@client.event 
async def on_ready():
    print("Najgorszy to kurwa ten Saper, zamiast wrócić to pisze sobie zastępcze Mydła")
    
#
@client.event
async def on_message(message):
    if message.content=="%napierdolony":
        await client.send_message(message.channel,"https://imgur.com/GNBuCbH")
    if message.content=="%au":
        await client.send_message(message.channel,"https://imgur.com/kDT4JVd")
    if message.content=="%test":
        await client.send_message(message.channel,"No pojebało cię Saper")
    if message.content=="%tfar":
        await client.send_message(message.channel,"Najlepszy")
    if message.content=="%acre":
        await client.send_message(message.channel,"Ssie")
    if message.content=="%mechy":
        await client.send_message(message.channel,"Wyjebać, nikt ich nie chce")
    if message.content=="%czapka":
        czapka=get(client.get_all_emojis(), name='dej_sombrero')
        await client.send_message(message.channel,czapka)
    if message.content=="%budowa":
        await client.send_message(message.channel,"!play https://www.youtube.com/watch?v=fCbaKnTLqf8")
    if message.content=="@everyone":
        emoji = get(client.get_all_emojis(), name='nachujpingujeszpedale')
        await client.add_reaction(message, emoji)
    if message.content=="%help":
        await client.send_message(message.channel,"DOSTĘPNE KOMENDY:")
        temp="```"
        for x in tabcom:
            temp=temp+x+"\n"
        temp=temp+"```"
        await client.send_message(message.channel,temp)

#


client.run("NTAyMTk5OTM4NTkyMTQ1NDE5.Dqke5A.qEYe0ZE7pEwk2V7qSgch09M_0SY") #token