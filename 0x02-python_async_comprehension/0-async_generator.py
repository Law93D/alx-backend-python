#!/usr/bin/env python3

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values() -> None:
    """
    Collects and prints values yielded by async_generator.
    """
    result: List[float] = []
    async for i in async_generator():
        result.append(i)
    print(result)

# Run the event loop manually
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_yielded_values())
