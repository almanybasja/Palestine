import os

from telethon import Button, events

from JE313P import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/1cf2e8eb817735b1c384b.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "AL515AT"
)

CAPTION = f"**سرعة البنك:** {ms}\n المالك:『{ALIVE}』"


@JE313P.on(events.NewMessage(pattern="^/بنك"))
async def _(event):
    UMM = [[Button.url("السورس", "https://t.me/AL515AT")]]
    await JE313P.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
