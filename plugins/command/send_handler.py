import re

from pyrogram import Client, enums, types

import config
from plugins import Database, Helper


async def send_with_pic_handler(
    client: Client, msg: types.Message, key: str, hastag: list
):
    db = Database(msg.from_user.id)
    helper = Helper(client, msg)
    user = db.get_data_pelanggan()

    if msg.from_user.is_bot:
        return await msg.reply(
            "Anda tidak diizinkan mengirimkan pesan sebagai bot.", quote=True
        )

    if msg.text or msg.photo or msg.video or msg.voice:
        menfess = user.menfess
        all_menfess = user.all_menfess
        coin = user.coin
        if menfess >= config.batas_kirim and user.status in [
            "member",
        ]:
          return await msg.reply(
              f"🙅🏻‍♀️ Post gagal terkirim. kamu hari ini telah mengirim ke menfess sebanyak {menfess}/{config.batas_kirim} kali.serta coin mu kurang untuk mengirim menfess diluar batas harian., kamu dapat mengirim menfess kembali pada hari esok.\n\n Waktu reset jam 1 pagi. \n\n\n\n Info: Topup Coin Hanya ke Admin",
                    quote=True,
                )

        link = await get_link()
        caption = msg.text or msg.caption
        # entities = msg.entities or msg.caption_entities

        kirim = await client.send_message(
            config.channel_1, caption
        )  # caption_entities=entities

        await helper.send_to_channel_log(type="log_channel", link=link + str(kirim.id))
        await db.update_menfess(coin, menfess, all_menfess)
        await msg.reply(
            f"Pesan telah berhasil terkirim. hari ini kamu telah mengirim menfess sebanyak {menfess + 1}/{config.batas_kirim} . kamu dapat mengirim menfess sebanyak {config.batas_kirim} kali dalam sehari\n\nWaktu reset setiap jam 1 pagi\n<a href='{link + str(kirim.id)}'>check pesan kamu</a>. \n\n\n\n Info: Topup Coin Hanya ke Admin"
        )
    else:
        await msg.reply("Media yang didukung photo, video dan voice")


async def send_menfess_handler(client: Client, msg: types.Message):
    helper = Helper(client, msg)
    db = Database(msg.from_user.id)
    db_user = db.get_data_pelanggan()
    db_bot = db.get_data_bot(client.id_bot).kirimchannel

    if msg.from_user.is_bot:
        return await msg.reply(
            "Anda tidak diizinkan mengirimkan pesan sebagai bot.", quote=True
        )

    if msg.text or msg.photo or msg.video or msg.voice:
        if msg.photo and not db_bot.photo:
            if db_user.status in ["member"]:
                return await msg.reply(
                    "Tidak bisa mengirim photo, karena sedang dinonaktifkan oleh admin",
                    True,
                )
        elif msg.video and not db_bot.video:
            if db_user.status in ["member"]:
                return await msg.reply(
                    "Tidak bisa mengirim video, karena sedang dinonaktifkan oleh admin",
                    True,
                )
        elif msg.voice and not db_bot.voice:
            if db_user.status in ["member"]:
                return await msg.reply(
                    "Tidak bisa mengirim voice, karena sedang dinonaktifkan oleh admin",
                    True,
                )

        menfess = db_user.menfess
        all_menfess = db_user.all_menfess
        coin = db_user.coin
        if menfess >= config.batas_kirim and db_user.status in [
            "member",
        ]:
          return await msg.reply(
              f"🙅🏻‍♀️ Post gagal terkirim. kamu hari ini telah mengirim ke menfess sebanyak {menfess}/{config.batas_kirim} kali.serta coin mu kurang untuk mengirim menfess diluar batas harian., kamu dapat mengirim menfess kembali pada hari esok.\n\n waktu reset jam 1 pagi. \n\n\n\n Info: Topup Coin Hanya ke Admin",
                    quote=True)

        link = await get_link()
        kirim = await client.copy_message(config.channel_1, msg.from_user.id, msg.id)
        await helper.send_to_channel_log(type="log_channel", link=link + str(kirim.id))
        await db.update_menfess(coin, menfess, all_menfess)
        await msg.reply(
            f"pesan telah berhasil terkirim. hari ini kamu telah mengirim menfess sebanyak {menfess + 1}/{config.batas_kirim} . kamu dapat mengirim menfess sebanyak {config.batas_kirim} kali dalam sehari\n\nwaktu reset setiap jam 1 pagi\n<a href='{link + str(kirim.id)}'>check pesan kamu</a>"
        )
    else:
        await msg.reply("Media yang didukung photo, video dan voice")


async def get_link():
    anu = str(config.channel_1).split("-100")[1]
    return f"https://t.me/c/{anu}/"


async def transfer_coin_handler(client: Client, msg: types.Message):
    if re.search(r"^[\/]tf_coin(\s|\n)*$", msg.text or msg.caption):
        err = (
            "<i>Perintah salah /tf_coin [jmlh_coin]</i>"
            if msg.reply_to_message
            else "<i>Perintah salah /tf_coin [id_user] [jmlh_coin]</i>"
        )
        return await msg.reply(err, True)
    helper = Helper(client, msg)
    if re.search(r"^[\/]tf_coin\s(\d+)(\s(\d+))?", msg.text or msg.caption):
        if x := re.search(r"^[\/]tf_coin\s(\d+)(\s(\d+))$", msg.text or msg.caption):
            target = x[1]
            coin = x[3]
        if y := re.search(r"^[\/]tf_coin\s(\d+)$", msg.text or msg.caption):
            if not msg.reply_to_message:
                return await msg.reply("Sambil mereply sebuah pesan", True)

            if msg.reply_to_message.from_user.is_bot == True:
                return await msg.reply("🤖Bot tidak dapat ditranfer coin", True)
            elif msg.reply_to_message.sender_chat:
                return await msg.reply("Channel tidak dapat ditranfer coin", True)
            else:
                target = msg.reply_to_message.from_user.id
                coin = y[1]
        if msg.from_user.id == int(target):
            return await msg.reply(
                "<i>Tidak dapat transfer coin untuk diri sendiri</i>", True
            )

        user_db = Database(msg.from_user.id)
        anu = user_db.get_data_pelanggan()
        my_coin = anu.coin
        if my_coin < int(coin):
            return await msg.reply(
                f"<i>Coin kamu ({my_coin}) tidak dapat transfer coin.</i>", True
            )
        db_target = Database(int(target))
        if not await db_target.cek_user_didatabase():
            return await msg.reply_text(
                text=f"<i><a href='tg://openmessage?user_id={str(target)}'>user</a> tidak terdaftar didatabase</i>",
                quote=True,
                parse_mode=enums.ParseMode.HTML,
            )
        target_db = db_target.get_data_pelanggan()
        ditransfer = my_coin - int(coin)
        diterima = target_db.coin + int(coin)
        nama = "Admin" if anu.status in ["owner", "admin"] else msg.from_user.first_name
        nama = await helper.escapeHTML(nama)
        try:
            await client.send_message(
                target,
                f"Coin berhasil ditambahkan senilai {coin} coin, Cek /status\n• Oleh <a href='tg://openmessage?user_id={msg.from_user.id}'>{nama}</a>",
            )
            await user_db.transfer_coin(
                ditransfer, diterima, target_db.coin_full, int(target)
            )
            await msg.reply(f"<i>Berhasil transfer coin sebesar {coin} coin💰</i>", True)
        except Exception as e:
            return await msg.reply_text(
                text=f"❌<i>Terjadi kesalahan, sepertinya user memblokir bot</i>\n\n{e}",
                quote=True,
                parse_mode=enums.ParseMode.HTML,
            )

    db = Database(msg.from_user.id)
    db_user = db.get_data_pelanggan()
    db_bot = db.get_data_bot(client.id_bot).kirimchannel
    if msg.text or msg.photo or msg.video or msg.voice:
        if msg.photo and not db_bot.photo:
            if db_user.status in ["member"]:
                return await msg.reply(
                    "Tidak bisa mengirim photo, karena sedang dinonaktifkan oleh admin",
                    True,
                )
        elif msg.video and not db_bot.video:
            if db_user.status in ["member"]:
                return await msg.reply(
                    "Tidak bisa mengirim video, karena sedang dinonaktifkan oleh admin",
                    True,
                )
        elif msg.voice and not db_bot.voice:
            if db_user.status in ["member"]:
                return await msg.reply(
                    "Tidak bisa mengirim voice, karena sedang dinonaktifkan oleh admin",
                    True,
                )

        menfess = db_user.menfess
        db_user.all_menfess
        coin = db_user.coin
        if menfess >= config.batas_kirim and db_user.status in [
            "member",
        ]:
            return await msg.reply(
                f"🙅🏻‍♀️ Post gagal terkirim. kamu hari ini telah mengirim ke menfess sebanyak {menfess}/{config.batas_kirim} kali.serta coin mu kurang untuk mengirim menfess diluar batas harian., kamu dapat mengirim menfess kembali pada hari esok.\n\n waktu reset jam 1 pagi. \n\n\n\n Info: Topup Coin Hanya ke Admin",
                    quote=True)
