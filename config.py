import os
from os import getenv


API_ID = int(os.environ.get("API_ID"))


API_HASH = os.environ.get("API_HASH")


BOT_TOKEN = os.environ.get("BOT_TOKEN")


OWNER_ID = list(
    map(int, getenv("OWNER_ID", "5738579437").split())
) 

#Fill Only Username Without @
SUPPORT_GROUP = getenv(
    "SUPPORT_GROUP", "Ur_support07"
)  

MONGO_URL = os.environ.get("MONGO_URL","mongodb+srv://BrandedSupportGroup:BRANDED_WORLD@cluster0.v4odcq9.mongodb.net/?retryWrites=true&w=majority")

LOGGER_ID = int(getenv("LOGGER_ID", "-1001992970818"))

# set True if you want yo set bot commands automatically 
SETCMD = getenv("SETCMD", "True")

# upstream repo 
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhopi/ChikuChatBot",
)

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

# GIT TOKEN ( if your edited repo is private)
GIT_TOKEN = getenv("GIT_TOKEN", None)
