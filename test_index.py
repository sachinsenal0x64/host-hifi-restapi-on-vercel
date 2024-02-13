import pytest

from src.index import root, get_track

@pytest.mark.asyncio
async def get_track():
    result = await get_track()
    assert result == result
