import config
from DEADLYSPAM import BOT0, deadlyversion, SUDOERS
from telethon import events, version, Button
from telethon.tl.custom import button

PIC = config.ALIVE_PIC

if config.ALIVE_PIC:
    DEADLY_PIC = PIC
else:
    DEADLY_PIC = "https://te.legra.ph/file/900b6cf283e7e1fc7667a.jpg"

hl = config.CMD_HNDLR


DEADLY = "✯ 𝗗𝐞𝐕𝐢𝐋 𝗦𝗽𝗮𝗺 𝗛𝗲𝗿𝗲 ✯\n\n"
DEADLY += f"═══════════════════\n"
DEADLY += f"• **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `4.0.0`\n"
DEADLY += f"• **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"
DEADLY += f"• **ᴅ𝙴𝚅𝙸𝙻ʟʏʙᴏᴛ ᴠᴇʀsɪᴏɴ**  : `{deadlyversion}`\n"
DEADLY += f"═══════════════════\n\n"   


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event): 
  if event.sender_id in SUDOERS:
     Blaze = [[Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/Classics0012"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/Classics002")]]
     await BOT0.send_file(event.chat_id, DEADLY_PIC, caption=DEADLY, buttons=Blaze) 
  else:
      await event.reply("**ᴅᴇᴘʟᴏʏ ʏᴏᴜʀ ᴏᴡɴ ᴅᴇᴀᴅʟʏ-ꜱᴘᴀᴍʙᴏᴛ!**") 
