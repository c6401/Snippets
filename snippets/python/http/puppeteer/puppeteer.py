import asyncio

from pyppeteer import launch
# from pyppeteer_stealth import stealth

async def func():
    browser = await launch({'headless': False})
    page = await browser.newPage()
    # await stealth(page)
    await page.goto('...')

    # await page.evaluate(
    #     f'''document.evaluate("//*[contains(text(), '...')]", '''
    #     '''document, null, XPathResult.ANY_TYPE, null).iterateNext().click()'''
    # )
    # await page.evaluate(f'''document.querySelector('...').click()''')

    await browser.close()

asyncio.get_event_loop().run_until_complete(func())
