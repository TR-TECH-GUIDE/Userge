# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020-2021 by SLBotsOfficial.
#
# This file is part of < https://github.com/TR-TECH-GUIDE/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TR-TECH-GUIDE/Userge/blob/master/LICENSE >
#
# All rights reserved.

import os

from userge import userge


async def _worker() -> None:
    chat_id = int(os.environ.get("CHAT_ID") or 0)
    type_ = 'unofficial' if os.path.exists("../userge/plugins/unofficial") else 'main'
    await userge.send_message(chat_id, f'`{type_} build completed !`')

if __name__ == "__main__":
    userge.begin(_worker())
    print('userge test has been finished!')
