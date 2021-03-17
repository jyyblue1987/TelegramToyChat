
import asyncio
import threading

from telethon.sync import TelegramClient, events

api_id = '3961096'
api_hash = '5c814390e26776fbe56919f7bff872cc'
channelId = 'https://t.me/testgrp_pi'

@asyncio.coroutine
def send_memssage(client):
    while True:
        msg = input()
        client.send_message(channelId, msg)  # needs async, I'm stuck!

def main():
    client = TelegramClient('my_listener', api_id, api_hash)
    client.start()

    # def send_message_thread():
    #     while True:
    #         msg = input()
    #         loop = asyncio.get_event_loop()
    #         loop.run_until_complete(my_async_def())
    #         client.send_message(channelId, msg)  # needs async, I'm stuck!

    # threading.Thread(target=send_message_thread).start()

    print('Running Telegram Listener...')

    @client.on(events.NewMessage(chats=channelId))
    async def handler(event):
        message = event.text
        print(message)

    print('flow into client event loop...')
    client.run_until_disconnected()


if __name__ == "__main__":
    main()