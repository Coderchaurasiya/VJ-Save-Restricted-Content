import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7510574909:AAHgqp_Kl4P-j0fzjZWvhplun0IlY7gh8z8")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "29091972"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "b12b66034ad60391a27aafa5cbc47f30")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://sonamex12:DAjDM7LHtIRANcYl@cluster0.tuppn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
