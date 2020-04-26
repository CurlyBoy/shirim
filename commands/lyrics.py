import requests, os, dataset, discord, re
from discord.ext import commands
from env import GENIUS_API_KEY
import lyricsgenius
genius = lyricsgenius.Genius(GENIUS_API_KEY)

def setup(bot):
    bot.add_cog(Lyrics(bot))

class Lyrics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lyrics(self, ctx, *args):
        artist = genius.search_artist(args[0], max_songs=1, sort="title")
        song = genius.search_song(args[1], artist.name)
        # await ctx.send(song.lyrics)
        # number_of_sections = song.lyrics.find("Above")
        sections = [i for i in range(len(song.lyrics)) if song.lyrics.startswith("[", i)] 
        await ctx.send(sections)
