import httpx


class Aioton:

    def __init__(self, api_key):
        self.url = "https://toncenter.com/api/v2/"
        self.__api_key = api_key
        self.__headers = {'X-API-Key': api_key}

    async def __check_error(self, array):
        if not array['ok']:
            raise Exception(str(array['error'] + " Code: " + str(array['code'])))
        else:
            return array

    async def get_address_info(self, address: str):
        async with httpx.AsyncClient() as client:
            r = await client.get(self.url + f"getAddressInformation?address={address}", headers=self.__headers)
            r = r.json()

            return await self.__check_error(r)

    async def get_extended_address_info(self, address: str):
        async with httpx.AsyncClient() as client:
            r = await client.get(self.url + f"getExtendedAddressInformation?address={address}", headers=self.__headers)
            r = r.json()

            return await self.__check_error(r)

    async def get_wallet_info(self, address: str):
        async with httpx.AsyncClient() as client:
            r = await client.get(self.url + f"getWalletInformation?address={address}", headers=self.__headers)
            r = r.json()

            return await self.__check_error(r)

    async def get_transactions(self, address: str, limit: int = 10, lt: int = None, hash_ex: str = "", to_lt: int = 0,
                               archival: bool = False):
        async with httpx.AsyncClient() as client:
            request_address = self.url + f"getTransactions?address={address}&limit={limit}&hash={hash_ex}" \
                                         f"&to_lt={to_lt}&archival={archival}"
            if lt:
                request_address += f"&lt={lt}"
            r = await client.get(request_address, headers=self.__headers)
            r = r.json()

            return await self.__check_error(r)

    async def get_address_balance(self, address: str):
        async with httpx.AsyncClient() as client:
            r = await client.get(self.url + f"getAddressBalance?address={address}", headers=self.__headers)
            r = r.json()

            return await self.__check_error(r)

    async def get_address_state(self, address: str):
        async with httpx.AsyncClient() as client:
            r = await client.get(self.url + f"getAddressState?address={address}", headers=self.__headers)
            r = r.json()

            return await self.__check_error(r)

    async def pack_address(self, address: str):
        async with httpx.AsyncClient() as client:
            r = await client.get(self.url + f"packAddress?address={address}", headers=self.__headers)
            r = r.json()

            return await self.__check_error(r)

    async def unpack_address(self, address: str):
        async with httpx.AsyncClient() as client:
            r = await client.get(self.url + f"unpackAddress?address={address}", headers=self.__headers)
            r = r.json()

            return await self.__check_error(r)

    async def detect_address(self, address: str):
        async with httpx.AsyncClient() as client:
            r = await client.get(self.url + f"detectAddress?address={address}", headers=self.__headers)
            r = r.json()

            return await self.__check_error(r)
