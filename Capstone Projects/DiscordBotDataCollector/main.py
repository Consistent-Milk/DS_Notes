# This is an example of a simple discord bot
# that can collect data and save it in google docs by simultaneously using 
# three different API's

# Our first capstone project will be based on this
# but it will be based on our own new discord server named 'Data science'

import discord
import gspread
import pandas as pd
import requests

TOKEN = #Secret#

credentials = {
    #Secret#
}


gc = gspread.service_account_from_dict(credentials)

sh = gc.open_by_url(
    "#Secret#")

worksheet = sh.get_worksheet(0)

intents = discord.Intents.all()

client = discord.Client(intents=intents)

intents = discord.Intents.all()
client = discord.Client(intents=intents)
guild = discord.Guild


@client.event
async def on_ready():
    print(f'Guild Bot is Online.')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.name == 'the-list':
        user_name = str(message.author.name).split('#')[0]
        user_message = str(message.content)
        link = user_message.split()[-1]

        if (len(user_message.split()) == 3):
            table = [user_name]
            fiction = user_message.split('/')[-1].split('?')[0]
            fiction = fiction.replace('-', ' ')
            fiction = fiction.title()
            for i in range(len(user_message.split())):
                table.append(user_message.split()[i])

            reviewId = link.split('review=')[1].split('#')[0]

            headers = {
                "X-API-Key": "#Secret#"}

            url = "#Secret API URL#" + reviewId
            soup = requests.get(url, headers=headers).json()
            date = soup['date'].split('T')[0]

            table.append(fiction)
            table.append(date)
            table.append('Verified')

            if (table[2].lower() == 'advanced') or (table[2].lower() == 'advanced,') or (table[2].lower() == 'advance'):
                table.append(2)
            else:
                table.append(1)

            worksheet.append_row(table)
        elif (len(user_message.split()) == 4):
            table = [user_name]
            fiction = user_message.split('/')[-1].split('?')[0]
            fiction = fiction.replace('-', ' ')
            fiction = fiction.title()
            table_data = user_message.split()
            
            table.append('-'.join(table_data[0:2]))
            table.append(table_data[2])
            table.append(table_data[3])
            reviewId = link.split('review=')[1].split('#')[0]

            headers = {
                "X-API-Key": "#Secret#"}

            url = "#Secret API URL#" + reviewId
            soup = requests.get(url, headers=headers).json()
            date = soup['date'].split('T')[0]

            table.append(fiction)
            table.append(date)
            table.append('Verified')

            if (table[2].lower() == 'advanced') or (table[2].lower() == 'advanced,') or (table[2].lower() == 'advance'):
                table.append(2)
            else:
                table.append(1)

            worksheet.append_row(table)

            await message.channel.send('WHY ARE YOU USING TWO WORDS FOR THE CATEGORY??!! Okay... I am fixing it for you this time.')

    if message.channel.name == 'guildbot-testing':

        user_name = str(message.author.name).split('#')[0]
        user_message = str(message.content)
        link = user_message.split()[-1]

        if (len(user_message.split()) == 3):
            table = [user_name]
            fiction = user_message.split('/')[-1].split('?')[0]
            fiction = fiction.replace('-', ' ')
            fiction = fiction.title()
            for i in range(len(user_message.split())):
                table.append(user_message.split()[i])

            reviewId = link.split('review=')[1].split('#')[0]

            headers = {
                "X-API-Key": "#Secret#"}

            url = "#Secret API URL#" + reviewId
            soup = requests.get(url, headers=headers).json()
            date = soup['date'].split('T')[0]

            table.append(fiction)
            table.append(date)
            table.append('Verified')

            if (table[2].lower() == 'advanced') or (table[2].lower() == 'advanced,'):
                table.append(2)
            else:
                table.append(1)

            worksheet.append_row(table)
        elif (len(user_message.split()) == 4):
            table = [user_name]
            fiction = user_message.split('/')[-1].split('?')[0]
            fiction = fiction.replace('-', ' ')
            fiction = fiction.title()
            table_data = user_message.split()
            
            table.append('-'.join(table_data[0:2]))
            table.append(table_data[2])
            table.append(table_data[3])
            reviewId = link.split('review=')[1].split('#')[0]

            headers = {
                "X-API-Key": "#Secret#"}

            url = "#Secret API URL#" + reviewId
            soup = requests.get(url, headers=headers).json()
            date = soup['date'].split('T')[0]

            table.append(fiction)
            table.append(date)
            table.append('Verified')

            if (table[2].lower() == 'advanced') or (table[2].lower() == 'advanced,') or (table[2].lower() == 'advance'):
                table.append(2)
            else:
                table.append(1)

            worksheet.append_row(table)

            await message.channel.send('WHY ARE YOU USING TWO WORDS FOR THE CATEGORY??!! Okay... I am fixing it for you this time.')
        
        elif (user_message == 'gimme-duck'):
            await message.channel.send('https://random-d.uk/api/v2/randomimg')


    if message.channel.name == 'check-the-list':
        user_message = str(message.content)
        
        if user_message.lower() == 'the-list':
            await message.channel.send('#Secret#')
client.run(TOKEN)
