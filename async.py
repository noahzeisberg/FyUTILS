import asyncio
import datetime

from requests_futures.sessions import FuturesSession


async def loop_requesting():
    print("Started!")
    while True:
        session = FuturesSession()
        content = session.get("https://pastebin.com/raw/Q2KvpaHu")
        print(content.result().content.decode())
        await asyncio.sleep(3)


async def main():
    await asyncio.gather(loop_requesting(), asyncio.to_thread(out))


def out():
    t = datetime.datetime.now().strftime("%H:%M:%S")

    while True:
        if datetime.datetime.now().strftime("%H:%M:%S") != t:
            t = datetime.datetime.now().strftime("%H:%M:%S")
            print(t)



asyncio.run(main())