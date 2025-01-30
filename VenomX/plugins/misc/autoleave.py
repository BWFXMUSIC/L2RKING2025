import asyncio
from datetime import datetime

from pyrogram.enums import ChatType

import config
from VenomX import app
from VenomX.core.call import Ayush, autoend
from VenomX.utils.database import get_client, is_active_chat, is_autoend


async def auto_leave():  
    if config.AUTO_LEAVING_ASSISTANT:
        while True:
            # Introducing sleep for 9000 seconds (adjust as needed)
            await asyncio.sleep(9000)
            
            from VenomX.core.userbot import assistants

            for num in assistants:
                client = await get_client(num)
                left = 0
                try:
                    async for i in client.get_dialogs():
                        if i.chat.type in [ChatType.SUPERGROUP, ChatType.GROUP, ChatType.CHANNEL]:
                            if (
                                i.chat.id != config.LOGGER_ID
                                and i.chat.id != -1001465277194
                                and i.chat.id != -1002120144597
                            ):
                                if left == 20:
                                    continue
                                if not await is_active_chat(i.chat.id):
                                    try:
                                        await client.leave_chat(i.chat.id)
                                        left += 1
                                    except:
                                        continue
                except Exception as e:
                    print(f"Error in auto_leave for {num}: {e}")


async def auto_end():  
    while True:
        # Sleep for 5 seconds between each check
        await asyncio.sleep(5)

        ender = await is_autoend()
        if not ender:
            continue
        
        for chat_id in autoend:
            timer = autoend.get(chat_id)
            if not timer:
                continue

            if datetime.now() > timer:
                if not await is_active_chat(chat_id):
                    autoend[chat_id] = {}
                    continue

                autoend[chat_id] = {}
                try:
                    await Ayush.stop_stream(chat_id)
                except Exception as e:
                    print(f"Error stopping stream in auto_end for {chat_id}: {e}")

                try:
                    await app.send_message(
                        chat_id,
                        "» ʙᴏᴛ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ʟᴇғᴛ ᴠɪᴅᴇᴏᴄʜᴀᴛ ʙᴇᴄᴀᴜsᴇ ɴᴏ ᴏɴᴇ ᴡᴀs ʟɪsᴛᴇɴɪɴɢ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ."
                    )
                except Exception as e:
                    print(f"Error sending message in auto_end for {chat_id}: {e}")


# Create tasks for both functions to run in parallel
async def main():
    asyncio.create_task(auto_leave())
    asyncio.create_task(auto_end())

# Start the asyncio event loop
if __name__ == "__main__":
    asyncio.run(main())
