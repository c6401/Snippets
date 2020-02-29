import httpx
import browsercookie
from urllib.parse import unquote

_COOKIES = browsercookie.firefox()  # chrome?

token = next(c for c in _COOKIES if 'perekrestok.accessToken' in c.name).value
async with httpx.AsyncClient() as client:
    response = await client.get(
        'https://my.perekrestok.ru/api/v4/...',
        headers={"X-Authorization": unquote(token)},
    )

response.json()
