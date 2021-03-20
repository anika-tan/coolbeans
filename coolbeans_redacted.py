from dotenv import load_dotenv
import os
import discord
import zenquotes


# get bot token from environmental variables
load_dotenv()
TOKEN = os.getenv('TOKEN')


intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents = intents)


slur_list = ["xxxxxx", "xxxxx", "xxxx", "xxxxx", "xxxxx", "xxx"]


@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

    
# assigns role when users join
@client.event
async def on_member_join(member):
    print("okkkk")
    print()
    print()
    print()
    role = discord.utils.get()


@client.event
async def on_message(message):

    # ignore if it's a message sent by bot
    if message.author == client.user:
        return None

    # greeting
    if message.content.startswith("-hi"):
        greeting = "Hello {0.author.mention}! I'm coolbeans :)".format(message)
        await message.channel.send(greeting)

    # catch slur words and inform mods
    #if any(word in message.content for word in slur_list):
    for slur in slur_list:
        if slur in message.content.lower():
            channel = client.get_channel([[REDACTED_CHANNEL_ID]]) # moderator-room channel, get ID
            await message.channel.send("That's not nice {0.author.mention} :(".format(message))
            await channel.send(
                """Hello <@&[[REDACTED_ROLE_ID]]>! User {0.author} seems to have broken a rule. \n \n The message: '{0.content}'. \n \n I detected this because of the word '{1}'.""".format(message, slur))
            break # make sure only one msg is sent

    # send inspirational quote
    if "bored" in message.content:
        quote = zenquotes.get_quote()
        await message.channel.send("""Hey there {0.author.mention}! Here's a quote: {1}""".format(message, quote))

# @client.event
# async def on_reaction_add(reaction, user):
#     if reaction.emoji == "👎":
#         print(reaction.message.content)

client.run(TOKEN)
