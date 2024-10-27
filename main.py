# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

import os

import requests

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
target_role_name = 'dev'

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$unban'):
        member = message.author
        target_role = discord.utils.get(member.guild.roles, name=target_role_name)
        if target_role not in member.roles:
            await message.channel.send(f'{member.mention} does not have the required role to use this command!')
            return
        m = message.content.split(' ')
        ip = m[1]
        payload = {'ip': ip}
        url = "https://meeatchicken.pythonanywhere.com/unban/bot"
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            print("Request successful!")
            print(response.text)
            await message.channel.send(f'{response.text}')
        else:
            print(f"Request failed with status code: {response.status_code}")
            await message.channel.send('ERROR')


    if message.content.startswith('$ban'):
        member = message.author
        target_role = discord.utils.get(member.guild.roles, name=target_role_name)
        if target_role not in member.roles:
            await message.channel.send(f'{member.mention} does not have the required role to use this command!')
            return
        m = message.content.split(' ')
        ip = m[1]
        payload = {'ip': ip}
        url = "https://meeatchicken.pythonanywhere.com/idk"
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            print("Request successful!")
            print(response.text)
            await message.channel.send(f'{response.text}')
        else:
            print(f"Request failed with status code: {response.status_code}")
            await message.channel.send('ERROR j')



    if message.content.startswith('$getban'):
        member = message.author
        target_role = discord.utils.get(member.guild.roles, name=target_role_name)
        if target_role not in member.roles:
            await message.channel.send(f'{member.mention} does not have the required role to use this command!')
            return
        ip = 'Nan'
        payload = {'ip': ip}
        url = "https://meeatchicken.pythonanywhere.com/get-bans"
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            print("Request successful!")
            print(response.text)
            await message.channel.send(f'{response.text}')
        else:
            print(f"Request failed with status code: {response.status_code}")
            await message.channel.send('ERROR j')



    if message.content.startswith('$help'):
        member = message.author
        await message.channel.send('$ban <ip>, $unban <ban_id>, $getban, $help')

    if message.content.startswith('$logs'):
        member = message.author
        target_role = discord.utils.get(member.guild.roles, name=target_role_name)
        if target_role not in member.roles:
            await message.channel.send(f'{member.mention} does not have the required role to use this command!')
            return
        ip = '1qaz622A'
        payload = {'password': ip}
        url = "https://meeatchicken.pythonanywhere.com/confirm/see"
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            print("Request successful!")
            print(response.text)
            await message.channel.send(f'{response.text}')
        else:
            print(f"Request failed with status code: {response.status_code}")
            await message.channel.send('ERROR')
try:
  token = os.getenv("TOKEN") or ""
  if token == "":
    raise Exception("Please add your token to the Secrets pane.")
  client.run(token)
except discord.HTTPException as e:
    if e.status == 429:
        print(
            "The Discord servers denied the connection for making too many requests"
        )
        print(
            "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
        )
    else:
        raise e

