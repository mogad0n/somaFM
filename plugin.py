###
# Copyright (c) 2020, mogad0n
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

from supybot import utils, plugins, ircutils, callbacks
from supybot.commands import *
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('SomaFM')
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x

import requests
import json

channels_url = 'https://somafm.com/channels.json'

class SomaFM(callbacks.Plugin):
    """Retrieves metadata from SomaFM"""

    @wrap([optional('something')])
    def SevenSoul(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[0]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/7soul.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f"2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f"3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f"4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f"5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional('something')])
    def bagel(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[1]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/bagel.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f"2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f"3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f"4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f"5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)


    @wrap([optional('something')])
    def beatblender(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[2]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/beatblender.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f"2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f"3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f"4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f"5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)


    @wrap([optional('something')])
    def bootliquor(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs .
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[3]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/bootliquor.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f"2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f"3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f"4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f"5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional('something')])
    def brfm(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[4]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/brfm.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f" 2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f" 3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f" 4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f" 5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional('something')])
    def cliqhop(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        irc.reply(re)
        calling <recent> will list the last 5 songs .
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[5]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/cliqhop.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f" 2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f" 3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f" 4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f" 5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)


    @wrap([optional('something')])
    def covers(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs .
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[6]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/covers.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f" 2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f" 3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f" 4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f" 5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional('something')])
    def deepspaceone(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[7]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/deepspaceone.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f" 2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f" 3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f" 4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f" 5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)


    @wrap([optional('something')])
    def defcon(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[8]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/defcon.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f"2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f"3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f"4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f"5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)


    @wrap([optional('something')])
    def digitalis(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[9]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/digitalis.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f"2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f"3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f"4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f"5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)


    @wrap([optional('something')])
    def dronezone(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[10]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/dronezone.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f"2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f"3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f"4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f"5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)


    @wrap([optional('something')])
    def dubstep(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[11]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/dubstep.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f"2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f"3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f"4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f"5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional('something')])
    def fluid(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[12]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/fluid.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f"2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f"3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f"4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f"5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional('something')])
    def folkfwd(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[13]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/folkfwd.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f"2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f"3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f"4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f"5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)


    @wrap([optional('something')])
    def groovesalad(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[14]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/groovesalad.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f"2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f"3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f"4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f"5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional('something')])
    def gsclassic(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[15]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/gsclassic.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f"2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f"3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f"4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f"5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)


    @wrap([optional('something')])
    def illstreet(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[16]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/illstreet.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f"2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f"3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f"4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f"5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional('something')])
    def indiepop(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[16]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/indiepop.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f"2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f"3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f"4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f"5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional('something')])
    def live(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[18]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/indiepop.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f"2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f"3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f"4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f"5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional('something')])
    def lush(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[19]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/lush.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f"2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f"3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f"4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f"5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)


    @wrap([optional('something')])
    def missioncontrol(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[20]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/missioncontrol.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f"2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f"3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f"4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f"5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)


    @wrap([optional('something')])
    def poptron(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[21]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/poptron.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f"2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f"3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f"4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f"5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional('something')])
    def secretagent(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[22]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/secretagent.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f"2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f"3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f"4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f"5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional('something')])
    def seventies(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[23]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/seventies.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f"2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f"3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f"4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f"5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional('something')])
    def sf1033(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[24]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/sf1033.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f"2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f"3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f"4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f"5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional('something')])
    def sonicuniverse(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[25]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/sonicuniverse.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f"2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f"3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f"4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f"5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional('something')])
    def spacestation(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[26]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/spacestation.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f"2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f"3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f"4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f"5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional('something')])
    def suburbsofgoa(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[27]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/suburbsofgoa.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f"2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f"3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f"4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f"5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional('something')])
    def thetrip(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[28]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/thetrip.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f"2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f"3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f"4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f"5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional('something')])
    def thistle(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[29]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/thistle.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f"2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f"3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f"4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f"5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional('something')])
    def u80s(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[30]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/u80s.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f"2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f"3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f"4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f"5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)


    @wrap([optional('something')])
    def metal(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[31]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/metal.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f"2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f"3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f"4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f"5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional('something')])
    def reggae(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[32]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/reggae.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f"2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f"3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f"4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f"5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional('something')])
    def scanner(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[33]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/scanner.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f"2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f"3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f"4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f"5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional('something')])
    def vaporwaves(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[34]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/vaporwaves.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f"2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f"3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f"4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f"5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional('something')])
    def specials(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chan_list = cont['channels']
            chanlist = chan_list[35]
            playlist_list = chanlist['playlist'][0]
            playlist = playlist_list['url']
            re = f"\x02{chanlist['title']}\x0f - \x02{chanlist['description']}\x0f, Genre: \x02{chanlist['genre']} by dj: \x02{chanlist['dj']}\x0f, Lastplayed: \x02{chanlist['lastplaying']}\x0f, Direct Stream Link: {playlist} | There are \x02{chanlist['listeners']}\x0f listeners to this stream"
        else:
            url = 'https://somafm.com/songs/specials.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. \x02{songs['songs'][0]['title']}\x0f by \x02{songs['songs'][0]['artist']}\x0f from \x02{songs['songs'][0]['album']}\x0f "
            re2 = f"2. \x02{songs['songs'][1]['title']}\x0f by \x02{songs['songs'][1]['artist']}\x0f from \x02{songs['songs'][1]['album']}\x0f "
            re3 = f"3. \x02{songs['songs'][2]['title']}\x0f by \x02{songs['songs'][2]['artist']}\x0f from \x02{songs['songs'][2]['album']}\x0f "
            re4 = f"4. \x02{songs['songs'][3]['title']}\x0f by \x02{songs['songs'][3]['artist']}\x0f from \x02{songs['songs'][3]['album']}\x0f "
            re5 = f"5. \x02{songs['songs'][4]['title']}\x0f by \x02{songs['songs'][4]['artist']}\x0f from \x02{songs['songs'][4]['album']}\x0f "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)


Class = SomaFM


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
