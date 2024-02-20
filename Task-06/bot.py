import discord
from discord.ext import commands
import datetime
from scraper import get_live_scores,team_1,team_2,match_status

token="MTIwNjI4NTY4MzY2NTQwMzkyNQ.GvOqEN.iQUB1e6JHTnTRmiCec2NcGwKKZR44PcoX9FC00"


intents = discord.Intents.default()
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

bot.remove_command('help')

@bot.command(name='livescore')
async def get_live_score(ctx):
    await ctx.send('Fetching live cricket scores...')

    score_data = get_live_scores()

    new_data = {
        'Team 1': team_1,
        'Team 2': team_2,
        'Match Status': match_status,
        'Date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    await ctx.send(f"{team_1}\n{team_2}\n{match_status}")
    await ctx.send(f"Current Date: {new_data['Date']}")

@bot.command(name='generate')
async def generate_csv(ctx):
    await ctx.send('Generating CSV file with live scores...')


@bot.command(name='help')
async def help_command(ctx):
    await ctx.send('List of available commands:\n'
                   '/livescore - To get live cricket scores\n'
                   '/generate - To generate CSV file with live scores\n'
                   '/help - To display this help message')


bot.run(token)