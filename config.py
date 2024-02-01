import os

from dotenv import load_dotenv

load_dotenv("config.env", override=True)

api_id = int(os.getenv("API_ID", 2040))
api_hash = os.getenv("API_HASH", "b18441a1ff607e10a989891a5462e627") 
bot_token = os.getenv("BOT_TOKEN")
# =========================================================== #

db_url = os.getenv("MONGODB_URL")
db_name = os.getenv("DATABASE_NAME")
# =========================================================== #

channel_1 = int(os.getenv("CHAT_ID_1"))
channel_2 = int(os.getenv("CHAT_ID_2"))
channel_log = int(os.getenv("LOG_CHAT_ID"))
# =========================================================== #

id_admin = int(os.getenv("ADMIN_ID"))
# =========================================================== #

batas_kirim = int(os.getenv("BATAS_KIRIM", 3))

# =========================================================== #


hastag = (
    os.getenv(
        "HASTAG",
        "#girl #boy #ask #spill #story #random #curhat #confess",
    )
    .replace(" ", "|")
    .lower()
)


pesan_join = os.getenv(
    "PESAN_JOIN", "Silahkan bergabung dengan kami terlebih dahulu."
)
start_msg = os.getenv(
    "PESAN_START",
    """"
{mention}, Silahkan kirim pesan anda menggunakan hastag dibawah ini :

• #girl [untuk identitas perempuan]
• #boy [untuk identitas laki laki]
• #ask [untuk bertanya]
• #spill [untuk spill masalah]
• #story [untuk berbagi cerita]

Contoh Pesan: #girl gabut bgt call yu (username)

{fullname} 🌱\n\nIni adalah bot menfess, semua pesan yang kamu kirim akan masuk ke channel secara anonymous. Ketik /help""",
)

gagalkirim_msg = os.getenv(
    "PESAN_GAGAL",
    """
{mention}, Silahkan kirim pesan anda menggunakan hastag dibawah ini :

• #girl [untuk identitas perempuan]
• #boy [untuk identitas laki laki]
• #ask [untuk bertanya]
• #spill [untuk spill masalah]
• #story [untuk berbagi cerita]

Contoh Pesan: #girl gabut bgt call yu (username)
""",
)
