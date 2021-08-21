from userge import userge, Message, Config, versions, get_version


@userge.on_cmd("repo", about={'header': "get repo link and details"})
async def see_repo(message: Message):
    """see repo"""
    output = f"""
**Hey**, __I am using__ 🔥 **Userge** from @SLBotsOfficial🔥

    __Durable as a Serge__

• **userge version** : `{get_version()}`
• **license** : {versions.__license__}
• **copyright** : {versions.__copyright__}
• **repo** : [Userge]({Config.UPSTREAM_REPO})
"""
    await message.edit(output)
