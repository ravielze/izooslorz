"""CONTOH DOANG: Source https://docs.python.org/3/library/asyncio-task.html"""
import asyncio
async def test():
    print('hello')
    await asyncio.sleep(3)
    print('world')
asyncio.run(test())