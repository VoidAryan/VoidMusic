#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

HELP_1 = """✘ **<u>Admin Commands:</u>**
◉ /pause - Pause Streaming.
◉ /resume - Resume The Paused Streaming.
◉ /skip - Skip Currently Playing.
◉ /end - Stop Streaming.
◉ /restart - Restart Bot From Chat.
  ┗ /cpause | /cresume | /cskip | /cstop - for channel play.

✘ <u>**Auth Users:**</u>
User can use admin command without admin rights in ur chat.

◉ /auth [Username] - Add Auth User in ur Chat.
◉ /unauth [Username] - Remove Auth User in ur Chat.
◉ /authusers - Check Auth List in ur Chat."""

HELP_2 = """✘ <u>**Play Commands:**</u>
◉ /play [query] - Playing Music.
◉ /vplay [query] - Playing Video.
◉ /cplay [query] - Channel Player.
◉ /player - Check Currently Playing in Group.
◉ /cplayer- Check Currently Playing in Channel.
◉ /channelplay [usname ch or id] - connect ur channel to group.

✘ **<u>Personal Playlist:</u>**
◉ /playlist - Check Your Saved Playlist.
◉ /deleteplaylist - Delete or Reset Your Playlist.
◉ /play - Without Query to Playing Your Playlist."""

HELP_3 = """✘ <u>**Bot Commands:**</u>

◉ /stats - Get Top 10 Tracks Global Stats, Top 10 Users of bot, Top 10 Chats on bot, Top 10 Played in a chat etc etc.
◉ /sudolist - Check Sudo Users of Bot
◉ /lyrics [Music Name] - Searches Lyrics for the particular Music on web.
◉ /song [Track Name] or [YT Link] - Download any track from youtube in mp3 or mp4 formats.
◉ /player -  Get a interactive Playing Panel.

**C** stands for channel play.

◉ /queue or /cqueue- Check Queue List of Streaming."""

HELP_4 = """✘ <u>**Extra  Commands:**</u>
◉ /start - Start the Music Bot.
◉ /help  - Get Commands Helper Menu with detailed explanations of commands.
◉ /ping- Ping the Bot For Checking Bot Response.
◉ /stats - Get Bot Stats.
◉ /sudolist - Check Sudo Users.
◉ /lyrics [Music Name] - Search Music Lyrics.
◉ /song [query] - Download Music or Video."""

HELP_5 = """✘ **<u>ADD & REMOVE SUDO USERS :</u>**
◉ /addsudo [Username or Reply to a user]
◉ /delsudo [Username or Reply to a user]

✘ **<u>HEROKU:</u>**
◉ /usage - Dyno Usage.

✘ **<u>CONFIG VARS:</u>**
◉ /get_var - Get a config var from Heroku or .env.
◉ /del_var - Delete any var on Heroku or .env.
◉ /set_var [Var Name] [Value] - Set a Var or Update a Var on heroku or .env. Seperate Var and its Value with a space.

✘ **<u>BOT COMMANDS:</u>**
◉ /reboot - Reboot your Bot. 
◉ /update - Update Bot.
◉ /speedtest - Check server speeds
◉ /maintenance [enable / disable] 
◉ /logger [enable / disable] - Bot logs the searched queries in logger group.
◉ /get_log [Number of Lines] - Get log of your bot from heroku or vps. Works for both.
◉ /autoend [enable|disable] - Enable Auto stream end after 3 mins if no one is listening.

✘ **<u>STATS COMMANDS:</u>**
◉ /activevoice - Check active voice chats on bot.
◉ /activevideo - Check active video calls on bot.
◉ /stats - Check Bots Stats

✘ **<u>BLACKLIST CHAT FUNCTION:</u>**
◉ /blacklistchat [CHAT_ID] - Blacklist any chat from using Music Bot
◉ /whitelistchat [CHAT_ID] - Whitelist any blacklisted chat from using Music Bot
◉ /blacklistedchat - Check all blacklisted chats.

✘ **<u>BLOCKED FUNCTION:</u>**
◉ /block [Username or Reply to a user] - Prevents a user from using bot commands.
◉ /unblock [Username or Reply to a user] - Remove a user from Bot's Blocked List.
◉ /blockedusers - Check blocked Users Lists

✘ **<u>GBAN FUNCTION:</u>**
◉ /gban [Username or Reply to a user] - Gban a user from bot's served chat and stop him from using your bot.
◉ /ungban [Username or Reply to a user] - Remove a user from Bot's gbanned List and allow him for using your bot
◉ /gbannedusers - Check Gbanned Users Lists

✘ **<u>VIDEOCALLS FUNCTION:</u>**
◉ /set_video_limit [Number of Chats] - Set a maximum Number of Chats allowed for Video Calls at a time. Default to 3 chats.
◉ /videomode [download|m3u8] - If download mode is enabled, Bot will download videos instead of playing them in M3u8 form. ByDefault to M3u8. You can use download mode when any query doesnt plays in m3u8 mode.

✘ **<u>PRIVATE BOT FUNCTION:</u>**
◉ /authorize [CHAT_ID] - Allow a chat for using your bot.
◉ /unauthorize [CHAT_ID] - Disallow a chat from using your bot.
◉/authorized - Check all allowed chats of your bot.

✘ **<u>BROADCAST FUNCTION:</u>**
◉ /broadcast [Message or Reply to a Message] - Broadcast any message to Bot's Served Chats.

<u>options for broadcast:</u>
**-pin** : This will pin your message 
**-pinloud** : This will pin your message with loud notification
**-user** : This will broadcast your message to the users who have started your bot.
**-assistant** : This will broadcast your message from assistant account of your bot.
**-nobot** : This will force your bot to not broadcast message

**Example:** `/broadcast -user -assistant -pin Hello Testing`

"""
