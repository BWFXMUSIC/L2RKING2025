from VenomX.core.bot import Ayush
from VenomX.core.dir import dirr
from VenomX.core.git import git
from VenomX.core.userbot import Userbot
from VenomX.misc import dbb, heroku
from .logging import LOGGER

# Function calls for initialization
dirr()
git()
dbb()
heroku()

# Create instances
app = Ayush()
userbot = Userbot()

# Platform APIs
from .platforms import AppleAPI, CarbonAPI, SoundAPI, SpotifyAPI, RessoAPI, TeleAPI, YouTubeAPI

apple = AppleAPI()
carbon = CarbonAPI()
soundcloud = SoundAPI()
spotify = SpotifyAPI()
resso = RessoAPI()
telegram = TeleAPI()
youtube = YouTubeAPI()
