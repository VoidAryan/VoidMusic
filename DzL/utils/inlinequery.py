#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="Youtube Search",
            description=f"Get YouTube video or music information from your query.",
            thumb_url="https://telegra.ph/file/a3866f5534588b97a9fc3.png",
            input_message_content=InputTextMessageContent("Give YouTube Music or Video Name."),
        ),
    ]
)
