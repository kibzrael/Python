import asyncio


def main():
    asyncio.run(hello())


async def hello():
    task = asyncio.create_task(foo())
    print(await task)
    print("Hello ...")
    await asyncio.sleep(2)
    print("... World!")


async def foo():
    await asyncio.sleep(1)
    print("Completed in foo")
    return "foo"


main()
