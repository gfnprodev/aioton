import asyncio

import aioton


ton = aioton.Aioton("Example")


async def main():

    t = await ton.detect_address("Address")
    print(t)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
