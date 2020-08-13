import asyncio
import pytest
import aiohttp

from ziggostatus import get_ziggo_status, ClientResponseError

pytestmark = pytest.mark.asyncio


async def testSuccessfulCall():
    session = aiohttp.ClientSession()

    # Test with valid postal code and house number
    assert await get_ziggo_status("1012JS", "1", session) == "No announcements or outages known"

    await session.close()


async def testUnsuccessfulCall():
    session = aiohttp.ClientSession()

    # Test with invalid postal code and house number
    with pytest.raises(ClientResponseError):
        await get_ziggo_status("1234AB", "99999", session)

    await session.close()

if __name__ == "__test__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(testSuccessfulCall())
    loop.run_until_complete(testUnsuccessfulCall())
