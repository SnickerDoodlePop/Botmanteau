#botmanteau v1.1 - a moderately annoying discord bot that creates portmanteaus out of user's messages

import discord
from random import randint
from key import BotToken

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def is_vowel(char: str) -> bool:
    return char.lower() in ('a', 'e', 'i', 'o', 'u')

def portManTeau(word: str, next_word: str) -> str:
    newWord: str = ""
    
    #append first word
    for letter in word:
        if is_vowel(letter):
            break
        
        else:
            newWord += letter
            
    #append second word
    secondPartIdx: int = 0
    for letter in next_word:
        if not is_vowel(letter):
            secondPartIdx += 1
            continue
        
        elif is_vowel(letter):
            newWord += next_word[secondPartIdx:]
            return newWord
            
def can_be_portmanteaued(word: str, next_word: str) -> bool:
    return      len(word) >= 2 \
            and len(next_word) >= 2 \
            and not is_vowel(next_word[0]) \
            and not is_vowel(word[0]) \
            and word != next_word \
            and word[0] != next_word[0]

@client.event
async def on_ready():
    print("Botmanteau V1.1 Online")

prevWords = []

@client.event
async def on_message(message: discord.Message = ""):
    try:
        print(f"message: {message.content}")
        words = message.content
        
        #wtf is this
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
        
        newWords = [word.lower() for word in words if word != "and" and word != "the"]
        words = newWords

        global prevWords

        for word in prevWords:
            if word in words:
                return

        prevWords = [word for word in words]
        
        for idx in range(len(words)):
            try:
                if can_be_portmanteaued(words[idx], words[idx+1]):
                    print("Plus it can be portmanteau'd!")
                    if randint(0, 2) >= 0 and len(message.content) <= 1000:
                        print(f"^^^^ that's a bingo!!")
                        #reply_msg = words[idx][0] + words[idx+1][1:]
                        reply_msg = words[idx] + " + " + words[idx + 1] + ": " + portManTeau(words[idx], words[idx+1])
                        await message.reply(reply_msg.lower())
                        return
            
            #this should never happen
            except IndexError:
                continue
            
    except Exception as e:
        print(Exception)
        
client.run(BotToken.KEY)