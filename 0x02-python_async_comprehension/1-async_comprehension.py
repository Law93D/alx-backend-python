#!/usr/bin/env python3
"""
1-async_comprehension.py - Defines async_comprehension coroutine.

This module contains a coroutine that uses async comprehensions to collect
random numbers asynchronously.
"""

from typing import List
from 0_async_generator import async_generator

async def async_comprehension() -> List[float]:
    """
    async_comprehension - Asynchronous comprehension coroutine.

    This coroutine collects 10 random numbers using an async comprehension
    over async_generator.

    Returns:
        List[float]: A list of 10 random numbers.
    """
    return [i async for i in async_generator()]

# Example usage
async def main():
    print(await async_comprehension())

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
