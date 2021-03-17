
import asyncio
import threading
import sys

from telethon.sync import TelegramClient, events

api_id = '3961096'
api_hash = '5c814390e26776fbe56919f7bff872cc'
channelId = 'https://t.me/testgrp_pi'

loop = asyncio.get_event_loop()

client = TelegramClient('my_listener', api_id, api_hash)
client.start()

async def async_input(prompt):
    """
    Python's ``input()`` is blocking, which means the event loop we set
    above can't be running while we're blocking there. This method will
    let the loop run while we wait for input.
    """
    print(prompt, end='', flush=True)
    return (await loop.run_in_executor(None, sys.stdin.readline)).rstrip()

async def main():

    print('Running Telegram Listener...')

    @client.on(events.NewMessage(chats=channelId))
    async def handler(event):
        message = event.text
        print(message)

    while True:
        # msg = await async_input('Enter a message: ')
        msg = (await loop.run_in_executor(None, sys.stdin.readline)).rstrip()
        await client.send_message(channelId, msg)

    client.run_until_disconnected()


if __name__ == "__main__":
    loop.run_until_complete(main())