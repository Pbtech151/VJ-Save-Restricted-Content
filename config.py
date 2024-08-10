import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "22354271"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "957a4eeb4d05144bd6c1838a44d7f1d6")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://Pbtech151:<pbtech@151>@pbtech151.ytbb8vs.mongodb.net/?retryWrites=true&w=majority&appName=Pbtech151")
