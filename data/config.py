from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = "5966956630:AAFr7iVMop_rKd-UPMoAYxOMjupCKIkzXEA"  # Bot toekn
ADMINS = [1004294567, ]  # adminlar ro'yxati
IP = "localhost"  # Xosting ip manzili

DB_USER = "nomoz"
DB_PASS = "31518"
DB_NAME = "nomoz"
DB_HOST = "localhost"
