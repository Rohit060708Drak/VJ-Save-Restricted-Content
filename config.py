import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8307441731:AAFZe1vdSOBlJqjsc1VHPttsxreqnLwzs6w")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "25910703"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "c3973154663a7b3c7d507dc1180b446f")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6000662798"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://darkeaglemovies_db_user:CDQBNG3HKbePFYQX@cluster0.dmnx8be.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
