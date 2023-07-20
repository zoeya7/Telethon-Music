from Zaid import Zaid, BOT_USERNAME
from Config import Config
from telethon import events, Button

PM_START_TEXT = """
𝗛𝗲𝗹𝗹𝗼 𝗧𝗵𝗲𝗿𝗲 {}
𝗜𝗺 𝘁𝗵𝗲 𝗣𝗶𝗻𝗸 𝗣𝗮𝗻𝘁𝗵𝗲𝗿 𝗶 𝗰𝗮𝗻 𝗺𝗮𝗸𝗲 𝘆𝗼𝘂 𝗵𝗮𝗽𝗽𝘆 𝗯𝘆 𝗽𝗹𝗮𝘆𝗶𝗻𝗴 𝗺𝘂𝘀𝗶𝗰 𝗶𝗻 𝘆𝗼𝘂𝗿 𝗴𝗿𝗼𝘂𝗽 𝗰𝗮𝗹𝗹𝘀, 𝘀𝗼 𝗯𝗮𝘀𝗶𝗰𝗮𝗹𝗹𝘆 𝗶'𝗺 𝗮 𝗺𝘂𝘀𝗶𝗰 𝗯𝗼𝘁.

𝗪𝗵𝗮𝘁 𝗺𝗮𝗸𝗲𝘀 𝗺𝗲 𝗱𝗶𝗳𝗳𝗲𝗿𝗲𝗻𝘁?
‣ 𝟮𝟰 ✘ 𝟳 𝗡𝗼𝗻 𝗦𝘁𝗼𝗽.
‣ 𝗡𝗼 𝗗𝗲𝗹𝗮𝘆.
‣ 𝗨𝗻𝗹𝗶𝗺𝗶𝘁𝗲𝗱 𝗦𝗼𝗻𝗴 𝗖𝗵𝗼𝗶𝗰𝗲𝘀.
‣ 𝗧𝗵𝗶𝘀 𝗯𝗼𝘁 𝗯𝗮𝘀𝗲𝗱 𝗼𝗻 𝘁𝗲𝗹𝗲𝘁𝗵𝗼𝗻. 𝗦𝗼 𝗶𝘁 𝗽𝗿𝗼𝘃𝗶𝗱𝗲 𝗺𝗼𝗿𝗲 𝘀𝘁𝗮𝗯𝗶𝗹𝗶𝘁𝘆 𝗳𝗿𝗼𝗺 𝗼𝘁𝗵𝗲𝗿 𝗯𝗼𝘁𝘀

𝗦𝘂𝗽𝗽𝗼𝗿𝘁 𝗚𝗿𝗼𝘂𝗽 @Musicbot_update 
🎼🎼🎼🎼🎼🎼🎼
𝙃𝙚𝙮 𝙒𝙖𝙣𝙩 𝙩𝙤 𝙢𝙖𝙠𝙚 𝙢𝙤𝙣𝙚𝙮? 𝘾𝙡𝙞𝙘𝙠 𝙧𝙚𝙜𝙞𝙨𝙩𝙚𝙧 𝙗𝙚𝙡𝙤𝙬
"""

@Zaid.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.client.send_file(event.chat_id,
             Config.START_IMG,
             caption=PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("➕ 𝐀𝐝𝐝 𝐦𝐞 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐜𝐡𝐚𝐭", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("📲 𝐑𝐞𝐠𝐢𝐬𝐭𝐞𝐫", f"http://www.9987up.cc/#/register?r_code=64326179373")],
        [Button.url("📁 𝐂𝐡𝐚𝐧𝐧𝐞𝐥", f"https://t.me/LittleTreasureTC"), Button.url("👤 𝐂𝐨𝐧𝐭𝐚𝐜𝐭", f"https://t.me/ZoeyaTC")],
        [Button.inline("ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅꜱ", data="help")]])
       return

    if event.is_group:
       await event.reply("**Hey Im online ✅**")
       return



@Zaid.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("➕ 𝐀𝐝𝐝 𝐦𝐞 𝐭𝐨 𝐲𝐨𝐮𝐫 𝐜𝐡𝐚𝐭", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("📲 𝐑𝐞𝐠𝐢𝐬𝐭𝐞𝐫", f"http://www.9987up.cc/#/register?r_code=64326179373")],
        [Button.url("📁 𝐂𝐡𝐚𝐧𝐧𝐞𝐥", f"https://t.me/LittleTreasureTC"), Button.url("👤 𝐂𝐨𝐧𝐭𝐚𝐜𝐭", f"https://t.me/ZoeyaTC")],
        [Button.inline("ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅꜱ", data="help")]])
       return


@Zaid.on(events.NewMessage(pattern="^[?!/]register$"))
async def start(event):
     if event.is_group:
       await event.reply("**https://www.9987up.cc/#/register?r_code=64326179373 📲**")
       return

@Zaid.on(events.NewMessage(pattern="^[?!/]money$"))
async def start(event):
     if event.is_group:
       await event.reply("**Come and check it out 🌐**",buttons=[
        [Button.url("Money Here", f"https://t.me/LittleTreasureTC")]])
       return

@Zaid.on(events.NewMessage(pattern="^[?!/]channel$"))
async def start(event):
     if event.is_group:
       await event.reply("**https://t.me/ZoeyaTC ✅**")
       return
