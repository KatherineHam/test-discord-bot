import discord
from discord.ext import commands
import os

# Set the bot's command prefix
intents = discord.Intents.default()
intents.message_content = True  # Enable reading message content
bot = commands.Bot(command_prefix="/", intents=intents)

# Folder containing the text files
TEXT_FILES_DIR = './txt_files'

# Function to search through text files for a keyword
def search_files(keyword):
    results = []
    # Go through each text file in the directory
    for filename in os.listdir(TEXT_FILES_DIR):
        if filename.endswith(".txt"):
            filepath = os.path.join(TEXT_FILES_DIR, filename)
            with open(filepath, 'r') as file:
                lines = file.readlines()
                # Check if the keyword is in any line of the file
                for line_number, line in enumerate(lines, 1):
                    if keyword.lower() in line.lower():  # Case insensitive search
                        results.append(f"Found in {filename} (Line {line_number}): {line.strip()}")
    return results

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.command(name="search")
async def search(ctx, *, keyword: str):
    # Search for the keyword in the text files
    results = search_files(keyword)
    if results:
        await ctx.send("\n".join(results))
    else:
        await ctx.send("No results found.")

# Run the bot with your token
bot.run('MTMxMzMxOTg3Mjc0NjIyNTcwNQ.G_iCfQ.M9vocDs8hh8V5l0Vrkkb0ka9GM5nDSfTcCxSZ4')
