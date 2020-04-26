import requests, os, dataset, discord, re
from discord.ext import commands
from env import GENIUS_API_KEY
import lyricsgenius
genius = lyricsgenius.Genius(GENIUS_API_KEY)
genius.remove_section_headers = True

def setup(bot):
    bot.add_cog(Lyrics(bot))

class Lyrics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lyrics(self, ctx, *args):
        # headers = {"Authorization": "Bearer " + GENIUS_API_KEY}

        # query_params = {
        #     "search": args[0]
        # }

        # genius_api = "https://api.genius.com/"
        # artist = requests.get(url=genius_api, headers=headers).json()
        # await ctx.send(artist)

        artist = genius.search_artist(args[0])
        await ctx.send(len(artist.songs))

        # song = genius.search_song(args[1], artist.name)

        # lines = ''
        # for line in song.lyrics.split('\n'):
        #     if line and not line.startswith('['):
        #         lines += line + "\n"
        # await ctx.send(lines)
