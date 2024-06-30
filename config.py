# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "29940662"))
API_HASH = getenv("API_HASH", "b9ccc26a417ce3a998d321086a2edbb6")
BOT_TOKEN = getenv("BOT_TOKEN", "7342412446:AAFef1NPW-GH6D8sFzQ6FxfJhCg_Dn02410")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1871785273").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://davata:boss@cluster0.jebhatr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002064268488")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002132785565"))
