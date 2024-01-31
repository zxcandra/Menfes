from pyrogram import Client, enums, types
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup)

import config  # Import config module for notification settings
from plugins import Database


async def send_notification(client, text):
    # Function to send notification to config.channel_1
    try:
        await client.send_message(config.channel_1, text)
    except Exception as e:
        print("Error sending notification:", str(e))


async def setting_handler(client: Client, msg: types.Message):
    db = Database(msg.from_user.id).get_data_bot(client.id_bot)
    pesan = (
        "<b>💌 Menfess User\n\n✅ = AKTIF\n❌ = TIDAK AKTIF</b>\n"
        + "______________________________\n\n"
    )
    photo = ["AKTIF", "✅"] if db.kirimchannel.photo else ["TIDAK AKTIF", "❌"]
    video = ["AKTIF", "✅"] if db.kirimchannel.video else ["TIDAK AKTIF", "❌"]
    voice = ["AKTIF", "✅"] if db.kirimchannel.voice else ["TIDAK AKTIF", "❌"]
    status_bot = "AKTIF" if db.bot_status else "TIDAK AKTIF"
    pesan += f"📸 Foto = <b>{photo[0]}</b>\n"
    pesan += f"🎥 Video = <b>{video[0]}</b>\n"
    pesan += f"🎤 Voice = <b>{voice[0]}</b>\n\n"
    pesan += f"🔰Status bot: <b> {status_bot}</b>"
    markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("📸", callback_data="no"),
                InlineKeyboardButton(photo[1], callback_data="photo"),
            ],
            [
                InlineKeyboardButton("🎥", callback_data="no"),
                InlineKeyboardButton(video[1], callback_data="video"),
            ],
            [
                InlineKeyboardButton("🎤", callback_data="no"),
                InlineKeyboardButton(voice[1], callback_data="voice"),
            ],
            [InlineKeyboardButton(status_bot, callback_data="status_bot")],
        ]
    )
    await msg.reply(
        pesan, quote=True, parse_mode=enums.ParseMode.HTML, reply_markup=markup
    )


async def photo_handler_inline(client: Client, query: CallbackQuery):
    msg = query.message
    inline_keyboard = msg.reply_markup.inline_keyboard[0][1].text
    my_db = Database(msg.from_user.id)
    if inline_keyboard in ["✅", "❌"]:
        pesan = "<b>💌 Menfess User\n\n✅ = AKTIF\n❌ = TIDAK AKTIF</b>\n"
        pesan += "______________________________\n\n"
        if inline_keyboard == "✅":
            await my_db.photo_handler("✅", client.id_bot)
        else:
            await my_db.photo_handler("❌", client.id_bot)

        db = my_db.get_data_bot(client.id_bot)
        photo = ["TIDAK AKTIF", "❌"] if not db.kirimchannel.photo else ["AKTIF", "✅"]
        video = ["TIDAK AKTIF", "❌"] if not db.kirimchannel.video else ["AKTIF", "✅"]
        voice = ["TIDAK AKTIF", "❌"] if not db.kirimchannel.voice else ["AKTIF", "✅"]
        status_bot = "TIDAK AKTIF" if not db.bot_status else "AKTIF"
        pesan += f"📸 Foto = <b>{photo[0]}</b>\n"
        pesan += f"🎥 Video = <b>{video[0]}</b>\n"
        pesan += f"🎤 Voice = <b>{voice[0]}</b>\n\n"
        pesan += f"🔰Status bot: <b>{status_bot}</b>"
        markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📸", callback_data="no"),
                    InlineKeyboardButton(photo[1], callback_data="photo"),
                ],
                [
                    InlineKeyboardButton("🎥", callback_data="no"),
                    InlineKeyboardButton(video[1], callback_data="video"),
                ],
                [
                    InlineKeyboardButton("🎤", callback_data="no"),
                    InlineKeyboardButton(voice[1], callback_data="voice"),
                ],
                [InlineKeyboardButton(status_bot, callback_data="status_bot")],
            ]
        )
        await msg.edit(pesan, parse_mode=enums.ParseMode.HTML, reply_markup=markup)


async def video_handler_inline(client: Client, query: CallbackQuery):
    msg = query.message
    inline_keyboard = msg.reply_markup.inline_keyboard[1][1].text
    my_db = Database(msg.from_user.id)
    if inline_keyboard in ["✅", "❌"]:
        pesan = "<b>💌 Menfess User\n\n✅ = AKTIF\n❌ = TIDAK AKTIF</b>\n"
        pesan += "______________________________\n\n"
        if inline_keyboard == "✅":
            await my_db.video_handler("✅", client.id_bot)
        else:
            await my_db.video_handler("❌", client.id_bot)

        db = my_db.get_data_bot(client.id_bot)
        photo = ["TIDAK AKTIF", "❌"] if not db.kirimchannel.photo else ["AKTIF", "✅"]
        video = ["TIDAK AKTIF", "❌"] if not db.kirimchannel.video else ["AKTIF", "✅"]
        voice = ["TIDAK AKTIF", "❌"] if not db.kirimchannel.voice else ["AKTIF", "✅"]
        status_bot = "TIDAK AKTIF" if not db.bot_status else "AKTIF"
        pesan += f"📸 Foto = <b>{photo[0]}</b>\n"
        pesan += f"🎥 Video = <b>{video[0]}</b>\n"
        pesan += f"🎤 Voice = <b>{voice[0]}</b>\n\n"
        pesan += f"🔰Status bot: <b>{status_bot}</b>"
        markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📸", callback_data="no"),
                    InlineKeyboardButton(photo[1], callback_data="photo"),
                ],
                [
                    InlineKeyboardButton("🎥", callback_data="no"),
                    InlineKeyboardButton(video[1], callback_data="video"),
                ],
                [
                    InlineKeyboardButton("🎤", callback_data="no"),
                    InlineKeyboardButton(voice[1], callback_data="voice"),
                ],
                [InlineKeyboardButton(status_bot, callback_data="status_bot")],
            ]
        )
        await msg.edit(pesan, parse_mode=enums.ParseMode.HTML, reply_markup=markup)


async def voice_handler_inline(client: Client, query: CallbackQuery):
    msg = query.message
    inline_keyboard = msg.reply_markup.inline_keyboard[2][1].text
    my_db = Database(msg.from_user.id)
    if inline_keyboard in ["✅", "❌"]:
        pesan = "<b>💌 Menfess User\n\n✅ = AKTIF\n❌ = TIDAK AKTIF</b>\n"
        pesan += "______________________________\n\n"
        if inline_keyboard == "✅":
            await my_db.voice_handler("✅", client.id_bot)
        else:
            await my_db.voice_handler("❌", client.id_bot)

        db = my_db.get_data_bot(client.id_bot)
        photo = ["TIDAK AKTIF", "❌"] if not db.kirimchannel.photo else ["AKTIF", "✅"]
        video = ["TIDAK AKTIF", "❌"] if not db.kirimchannel.video else ["AKTIF", "✅"]
        voice = ["TIDAK AKTIF", "❌"] if not db.kirimchannel.voice else ["AKTIF", "✅"]
        status_bot = "TIDAK AKTIF" if not db.bot_status else "AKTIF"
        pesan += f"📸 Foto = <b>{photo[0]}</b>\n"
        pesan += f"🎥 Video = <b>{video[0]}</b>\n"
        pesan += f"🎤 Voice = <b>{voice[0]}</b>\n\n"
        pesan += f"🔰Status bot: <b>{status_bot}</b>"
        markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📸", callback_data="no"),
                    InlineKeyboardButton(photo[1], callback_data="photo"),
                ],
                [
                    InlineKeyboardButton("🎥", callback_data="no"),
                    InlineKeyboardButton(video[1], callback_data="video"),
                ],
                [
                    InlineKeyboardButton("🎤", callback_data="no"),
                    InlineKeyboardButton(voice[1], callback_data="voice"),
                ],
                [InlineKeyboardButton(status_bot, callback_data="status_bot")],
            ]
        )
        await msg.edit(pesan, parse_mode=enums.ParseMode.HTML, reply_markup=markup)


async def status_handler_inline(client: Client, query: CallbackQuery):
    msg = query.message
    inline_keyboard = msg.reply_markup.inline_keyboard[3][0].text
    my_db = Database(msg.from_user.id)
    if inline_keyboard in ["AKTIF", "TIDAK AKTIF"]:
        pesan = "<b>💌 Menfess User\n\n✅ = AKTIF\n❌ = TIDAK AKTIF</b>\n"
        pesan += "______________________________\n\n"
        if inline_keyboard == "AKTIF":
            await my_db.bot_handler("off")
        else:
            await my_db.bot_handler("on")

        db = my_db.get_data_bot(client.id_bot)
        photo = ["TIDAK AKTIF", "❌"] if not db.kirimchannel.photo else ["AKTIF", "✅"]
        video = ["TIDAK AKTIF", "❌"] if not db.kirimchannel.video else ["AKTIF", "✅"]
        voice = ["TIDAK AKTIF", "❌"] if not db.kirimchannel.voice else ["AKTIF", "✅"]
        status_bot = "TIDAK AKTIF" if not db.bot_status else "AKTIF"
        pesan += f"📸 Foto = <b>{photo[0]}</b>\n"
        pesan += f"🎥 Video = <b>{video[0]}</b>\n"
        pesan += f"🎤 Voice = <b>{voice[0]}</b>\n\n"
        pesan += f"🔰Status bot: <b>{status_bot}</b>"
        markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📸", callback_data="no"),
                    InlineKeyboardButton(photo[1], callback_data="photo"),
                ],
                [
                    InlineKeyboardButton("🎥", callback_data="no"),
                    InlineKeyboardButton(video[1], callback_data="video"),
                ],
                [
                    InlineKeyboardButton("🎤", callback_data="no"),
                    InlineKeyboardButton(voice[1], callback_data="voice"),
                ],
                [InlineKeyboardButton(status_bot, callback_data="status_bot")],
            ]
        )
        await msg.edit(pesan, parse_mode=enums.ParseMode.HTML, reply_markup=markup)
