# europarl
Python client for accessing and analyzing European Parliament data

## Europarl Swagger
https://data.europarl.europa.eu/en/developer-corner/opendata-api

## Installation
`pip install https://github.com/robincvlr/europarl.git`

## Example
```
from europarl.client import EuroparlClient

async with EuroparlClient() as client:
    status, data = await client.get(
        query="meps/show-current",
        limit=10,
        offset=0,
        country_of_representation="FR",
        format="application/ld+json",
    )
```
