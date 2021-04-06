import asyncio
import sys
from telethon.sync import TelegramClient, events
import re
import webbrowser

api_id = '3961096'
api_hash = '5c814390e26776fbe56919f7bff872cc'
channelId = 'https://t.me/testgrp_pi'

api_id = 3743452
api_hash = 'f65ae54bdbf263c003de4315b1165de8'
channelId = 'https://t.me/MDXTrading'

def findUrls(url):
    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', url)
    return urls


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

    urls = findUrls(message)
    for url in urls:
        webbrowser.open(url, new=2)


if __name__ == "__main__":

    client = CLITelegram('my_listener', api_id, api_hash, on_message)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(client.run())