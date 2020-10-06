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

    @wrap([optional("literal", ("recent"))])
    def SevenSoul(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/7soul.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f"2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f"3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f"4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f"5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional("literal", ("recent"))])
    def bagel(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/bagel.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f"2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f"3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f"4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f"5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)


    @wrap([optional("literal", ("recent"))])
    def beatblender(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/beatblender.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f"2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f"3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f"4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f"5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)


    @wrap([optional("literal", ("recent"))])
    def bootliquor(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs .
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/bootliquor.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f"2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f"3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f"4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f"5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional("literal", ("recent"))])
    def brfm(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/brfm.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f" 2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f" 3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f" 4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f" 5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional("literal", ("recent"))])
    def cliqhop(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        irc.reply(re)
        calling <recent> will list the last 5 songs .
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/cliqhop.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f" 2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f" 3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f" 4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f" 5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)


    @wrap([optional("literal", ("recent"))])
    def covers(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs .
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/covers.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f" 2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f" 3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f" 4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f" 5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional("literal", ("recent"))])
    def deepspaceone(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/deepspaceone.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f" 2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f" 3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f" 4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f" 5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)


    @wrap([optional("literal", ("recent"))])
    def defcon(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/defcon.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f"2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f"3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f"4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f"5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)


    @wrap([optional("literal", ("recent"))])
    def digitalis(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/digitalis.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f"2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f"3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f"4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f"5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)


    @wrap([optional("literal", ("recent"))])
    def dronezone(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/dronezone.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f"2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f"3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f"4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f"5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)


    @wrap([optional("literal", ("recent"))])
    def dubstep(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/dubstep.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f"2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f"3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f"4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f"5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional("literal", ("recent"))])
    def fluid(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/fluid.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f"2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f"3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f"4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f"5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional("literal", ("recent"))])
    def folkfwd(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/folkfwd.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f"2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f"3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f"4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f"5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)


    @wrap([optional("literal", ("recent"))])
    def groovesalad(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/groovesalad.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f"2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f"3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f"4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f"5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional("literal", ("recent"))])
    def gsclassic(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/gsclassic.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f"2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f"3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f"4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f"5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)


    @wrap([optional("literal", ("recent"))])
    def illstreet(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/illstreet.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f"2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f"3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f"4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f"5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional("literal", ("recent"))])
    def indiepop(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/indiepop.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f"2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f"3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f"4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f"5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional("literal", ("recent"))])
    def live(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/indiepop.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f"2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f"3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f"4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f"5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional("literal", ("recent"))])
    def lush(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/lush.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f"2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f"3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f"4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f"5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)


    @wrap([optional("literal", ("recent"))])
    def missioncontrol(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/missioncontrol.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f"2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f"3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f"4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f"5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)


    @wrap([optional("literal", ("recent"))])
    def poptron(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/poptron.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f"2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f"3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f"4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f"5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional("literal", ("recent"))])
    def secretagent(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/secretagent.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f"2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f"3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f"4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f"5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional("literal", ("recent"))])
    def seventies(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/seventies.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f"2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f"3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f"4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f"5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional("literal", ("recent"))])
    def sf1033(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs.
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/sf1033.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f"2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f"3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f"4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f"5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional("literal", ("recent"))])
    def sonicuniverse(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/sonicuniverse.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f"2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f"3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f"4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f"5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional("literal", ("recent"))])
    def spacestation(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/spacestation.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f"2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f"3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f"4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f"5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional("literal", ("recent"))])
    def suburbsofgoa(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/suburbsofgoa.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f"2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f"3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f"4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f"5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional("literal", ("recent"))])
    def thetrip(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/thetrip.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f"2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f"3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f"4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f"5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional("literal", ("recent"))])
    def thistle(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/thistle.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f"2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f"3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f"4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f"5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional("literal", ("recent"))])
    def u80s(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/u80s.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f"2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f"3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f"4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f"5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)


    @wrap([optional("literal", ("recent"))])
    def metal(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/metal.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f"2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f"3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f"4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f"5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional("literal", ("recent"))])
    def reggae(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/reggae.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f"2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f"3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f"4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f"5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional("literal", ("recent"))])
    def scanner(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/scanner.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f"2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f"3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f"4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f"5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional("literal", ("recent"))])
    def vaporwaves(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/vaporwaves.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f"2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f"3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f"4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f"5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)

    @wrap([optional("literal", ("recent"))])
    def specials(self, irc, msg, args, recent):
        """[<recent>]

        Retrieves channel information including the playlist
        calling <recent> will list the last 5 songs
        """
        if not recent:
            r = requests.get(channels_url)
            cont = json.loads(r.content)
            chanlist = cont['channels']
            playlist = chanlist['playlist'][0]['url']
            re = f"{chanlist['title']} - {chanlist['description']}, Genre: {chanlist['genre']} by dj: {chanlist['dj']}, Lastplayed: {chanlist['lastplaying']}, Direct Stream Link: {playlist} | There are {chanlist['listeners']} listeners to this stream"
        else:
            url = 'https://somafm.com/songs/specials.json'
            req = requests.get(url)
            songs = json.loads(req.content)
            radio = songs['id']
            re1 = f" 1. {songs['songs'][0]['title']} by {songs['songs'][0]['artist']} from {songs['songs'][0]['album']} "
            re2 = f"2. {songs['songs'][1]['title']} by {songs['songs'][1]['artist']} from {songs['songs'][1]['album']} "
            re3 = f"3. {songs['songs'][2]['title']} by {songs['songs'][2]['artist']} from {songs['songs'][2]['album']} "
            re4 = f"4. {songs['songs'][3]['title']} by {songs['songs'][3]['artist']} from {songs['songs'][3]['album']} "
            re5 = f"5. {songs['songs'][4]['title']} by {songs['songs'][4]['artist']} from {songs['songs'][4]['album']} "
            re = radio + re1 + re2 + re3 + re4 + re5
        irc.reply(re)


Class = SomaFM


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
