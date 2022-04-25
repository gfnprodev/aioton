import asyncio

import aioton


ton = aioton.Aioton("api key")


async def main():
    t = await ton.detect_address("address")
    print(t)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
