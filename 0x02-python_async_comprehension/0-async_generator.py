#!/usr/bin/env python3
"""
0-async_generator.py - Defines async_generator coroutine.

This module contains a coroutine that generates random numbers asynchronously.
"""

import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """
    async_generator - Asynchronous generator coroutine.

    This coroutine loops 10 times, each time asynchronously waits 1 second,
    then yields a random number between 0 and 10.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

# Example usage
async def main():
    async for num in async_generator():
        print(num)

if __name__ == "__main__":
    asyncio.run(main())
