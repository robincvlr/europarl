import asyncio
import http
import unittest

from src.client import EuroparlClient


class TestEuroparlClient(unittest.TestCase):

    def test_get_datasets(self):
        # Test the get method
        async def test():
            async with EuroparlClient() as client:
                status, data = await client.get(
                    query="meps/show-current",
                    limit=10,
                    offset=0,
                    country_of_representation="FR",
                    format="application/ld+json",
                )

                # Assert that the response status code is 200
                self.assertEqual(status, http.HTTPStatus.OK)

                # Assert that the "data" array is not empty
                self.assertTrue("data" in data, "'data' key is missing in the response")
                self.assertGreater(len(data["data"]), 0, "'data' array is empty")

        # Run the async test
        asyncio.run(test())


if __name__ == "__main__":
    unittest.main()
