from pyrogram.types import InlineKeyboardButton
from X import CMD_HELP
class Data:

    text_help_menu = (
        "**𝐌𝐞𝐧𝐮 𝐈𝐧𝐥𝐢𝐧𝐞 𝐀𝐊-𝐊𝐈𝐍𝐆-𝐔𝐬𝐞𝐫𝐛𝐨𝐭**\n**Prefixes:** ., ?, !, *"
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("'", "")
    )
    reopen = [[InlineKeyboardButton("See more", callback_data="reopen")]]
