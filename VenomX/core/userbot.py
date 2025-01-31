import sys
from pyrogram import Client
import config
from ..logging import LOGGER

assistants = []
assistantids = []

class Userbot(Client):
    def __init__(self):
        self.clients = {
            "one": Client(name="VenomXAss1", api_id=config.API_ID, api_hash=config.API_HASH, session_string=str(config.STRING1), no_updates=True),
            "two": Client(name="VenomXAss2", api_id=config.API_ID, api_hash=config.API_HASH, session_string=str(config.STRING2), no_updates=True),
            "three": Client(name="VenomXAss3", api_id=config.API_ID, api_hash=config.API_HASH, session_string=str(config.STRING3), no_updates=True),
            "four": Client(name="VenomXAss4", api_id=config.API_ID, api_hash=config.API_HASH, session_string=str(config.STRING4), no_updates=True),
            "five": Client(name="VenomXAss5", api_id=config.API_ID, api_hash=config.API_HASH, session_string=str(config.STRING5), no_updates=True),
        }

    async def start_assistant(self, assistant_number, client, session_string):
        """Helper function to start an assistant and join chats."""
        try:
            LOGGER.info(f"Starting Assistant {assistant_number}...")

            # Start the client (assistant)
            await client.start()

            # Join the necessary chats
            try:
                await client.join_chat("BWF_MUSIC1")
                await client.join_chat("MUSICBOT_OWNER")
            except Exception as e:
                LOGGER.error(f"Assistant {assistant_number} failed to join chat: {str(e)}")

            assistants.append(assistant_number)

            # Fetch the assistant's details
            get_me = await client.get_me()
            client.username = get_me.username
            client.id = get_me.id
            assistantids.append(get_me.id)

            # Set the assistant's name
            client.name = f"{get_me.first_name} {get_me.last_name}" if get_me.last_name else get_me.first_name

            LOGGER.info(f"Assistant {assistant_number} started as {client.name}")

            # Send a log message to the logger group
            try:
                await client.send_message(
                    config.LOGGER_ID, 
                    f"**» Assistant {assistant_number} Started:**\n\n✨ ID: `{client.id}`\n❄ Name: {client.name}\n💫 Username: @{client.username}"
                )
            except Exception as e:
                LOGGER.error(f"Assistant {assistant_number} failed to send a log message: {str(e)}")

        except Exception as e:
            LOGGER.error(f"Assistant {assistant_number} failed to start: {str(e)}")
            sys.exit()

    async def start(self):
        """Main method to start all assistants."""
        LOGGER.info("Getting Assistants Info...")

        # Check for each assistant's session string in the config and start it if available
        for assistant_number, (assistant_name, client) in enumerate(self.clients.items(), start=1):
            if getattr(config, f"STRING{assistant_number}", None):
                await self.start_assistant(assistant_number, client, getattr(config, f"STRING{assistant_number}"))
