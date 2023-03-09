#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import os
from typing import List

import yaml

languages = {}
commands = {}


def get_command(value: str) -> List:
    return commands["command"][value]


def get_string(lang: str):
    return languages[lang]


for filename in os.listdir(r"./strings"):
    if filename.endswith(".yml"):
        language_name = filename[:-4]
        commands[language_name] = yaml.safe_load(
            open(r"./strings/" + filename, encoding="utf8")
        )


for filename in os.listdir(r"./strings/langs/"):
    if "id" not in languages:
        languages["id"] = yaml.safe_load(
            open(r"./strings/langs/id.yml", encoding="utf8")
        )
    if filename.endswith(".yml"):
        language_name = filename[:-4]
        if language_name == "id":
            continue
        languages[language_name] = yaml.safe_load(
            open(r"./strings/langs/" + filename, encoding="utf8")
        )
        for item in languages["id"]:
            if item not in languages[language_name]:
                languages[language_name][item] = languages["id"][item]
