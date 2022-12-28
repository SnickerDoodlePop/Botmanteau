#botmanteau v1.1 - a moderately annoying discord bot that creates portmanteaus out of user's messages
#adapted from botmanteau by Samson Morrow

import discord
from random import randint

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def is_vowel(char: str) -> bool:
    return char.lower() in ('a', 'e', 'i', 'o', 'u')

def can_be_portmanteaued(word: str, next_word: str) -> bool:
    return (len(word) >= 3) and (len(next_word) >= 3) and is_vowel(word[1]) and is_vowel(next_word[1]) and (not is_vowel(next_word[0])) and (not is_vowel(word[0])) and (word != next_word) and (word[0] != next_word[0])

@client.event
async def on_ready():
    print("Botmanteau V1.1 Online")

@client.event
async def on_message(message: discord.Message = ""):

    print(f"message: {message.content}")
    words = message.content
    
    words = words.replace('\"','')
    words = words.replace(',','')
    words = words.replace('.','')
    words = words.replace('/','')
    words = words.replace('\\','')
    words = words.replace('!','')
    words = words.replace('@','')
    words = words.replace('#','')
    words = words.replace('$','')
    words = words.replace('%','')
    words = words.replace('^','')
    words = words.replace('&','')
    words = words.replace('*','')
    words = words.replace('(','')
    words = words.replace(')','')
    words = words.replace('[','')
    words = words.replace(']','')
    words = words.replace('\[','')
    words = words.replace('\]','')
    words = words.replace('\n','')
    
    words = words.strip().split()

    for idx in range(len(words)):
        try:
            if can_be_portmanteaued(words[idx], words[idx+1]):
                print("Plus it can be portmanteau'd!")
                if randint(0, 2) >= 0 and len(message.content) <= 1000:
                    print(f"^^^^ that's a bingo!!")
                    reply_msg = words[idx][0] + words[idx+1][1:]
                    await message.reply(reply_msg.lower())
                    return
            
        except IndexError:
            continue
        
client.run("Your bot token here")