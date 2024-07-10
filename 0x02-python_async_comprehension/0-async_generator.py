#!/usr/bin/env python3
"""
0-async_generator.py - Defines async_generator coroutine.

This module contains a coroutine that generates random numbers asynchronously.
"""

import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """Generates random numbers between 0 and 10 asynchronously."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

def main():
    """Entry point for the script."""
    result = asyncio.run(async_generator())
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
