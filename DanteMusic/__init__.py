from SafoneAPI import SafoneAPI
from DanteMusic.core.bot import DanteBot
from DanteMusic.core.dir import dirr
from DanteMusic.core.git import git
from DanteMusic.core.userbot import Userbot
from DanteMusic.misc import dbb, heroku, sudo
from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()
api = SafoneAPI()
# Bot Client
app = DanteBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
HELPABLE = {}
