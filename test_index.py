import pytest
import json

from src.index import root, get_track

@pytest.mark.asyncio
async def test_get_track():
    result = await get_track()
    assert result == result.json()
