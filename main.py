import asyncio
import sys
from telethon.sync import TelegramClient, events

api_id = '3961096'
api_hash = '5c814390e26776fbe56919f7bff872cc'
channelId = 'https://t.me/testgrp_pi'

class CLITelegram(TelegramClient):
    def __init__(self, session_user_id, api_id, api_hash, on_message):
        super().__init__(session_user_id, api_id, api_hash)
        self.on_message = on_message
        self.start()

    async def message_handler(self, event):
        self.on_message(event.text)

    async def run(self):
        self.add_event_handler(self.message_handler, events.NewMessage)

        while True:
            # msg = await async_input('Enter a message: ')
            msg = (await loop.run_in_executor(None, sys.stdin.readline)).rstrip()
            if msg != "":
                await self.send_message(channelId, msg)

        self.run_until_disconnected()

def on_message(message):
    print(message)

if __name__ == "__main__":
    client = CLITelegram('my_listener', api_id, api_hash, on_message)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(client.run())