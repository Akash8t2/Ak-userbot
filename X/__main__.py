import importlib
from pyrogram import idle
from uvloop import install


from X.modules import ALL_MODULES
from X import BOTLOG_CHATID, LOGGER, LOOP, aiosession, app, bots, ids, bot1
from X.helpers import join
from X.helpers.misc import create_botlog, heroku

BOT_VER = "2.0.0"
CMD_HANDLER = ["." "?" "!" "*"]
MSG_ON = """
〆 **Japanese-X-Userbot is active** 〆
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
㋱ **Userbot Version -** `{}`
㋱ **Type** `{}alive` **to Check Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""


async def main():
    await app.start()
    print("LOG: Founded Bot token Booting..")
    for all_module in ALL_MODULES:
        importlib.import_module("X.modules" + all_module)
        print(f"Successfully Imported {all_module} ")
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            await join(bot)
            try:
                await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER))
            except BaseException:
                pass
            print(f"Started as {ex.first_name} | {ex.id} ")
            ids.append(ex.id)
        except Exception as e:
            print(f"{e}")
    if not str(BOTLOG_CHATID).startswith("-100"):
        await create_botlog(bot1)
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("X").info("Japanese-X-Userbot is Active, Dick🐣")
    install()
    heroku()
    LOOP.run_until_complete(main())
