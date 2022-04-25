import asyncio

import aioton


ton = aioton.Aioton("c9a7c91520e07e86e5959ed58f3494ae7f968d2bbea21e2aae3cb37d74686a95")


async def test():
    try:
        t = await ton.detect_address("EQAD3bDolMTBAQuh-nLiPsCXK1RN-aHa00pqhs92yu3w5YlL")
    except Exception as e:
        print(e)
    else:
        print(t)

l = asyncio.get_event_loop()
l.run_until_complete(test())