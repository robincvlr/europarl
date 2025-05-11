import http

import pytest

from europarl.client import EuroparlClient


@pytest.mark.asyncio
async def test_get_datasets():
    async with EuroparlClient() as client:
        status, data = await client.get(
            query="meps/show-current",
            limit=10,
            offset=0,
            country_of_representation="FR",
            format="application/ld+json",
        )

        assert status == http.HTTPStatus.OK
        assert "data" in data
        assert len(data["data"]) > 0
