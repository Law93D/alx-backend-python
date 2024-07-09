#!/usr/bin/env python3
"""
2-measure_runtime.py - Measures runtime of async_comprehension in parallel.

This module measures the total runtime of executing async_comprehension four
times in parallel using asyncio.gather().
"""

import asyncio
import time
from 1_async_comprehension import async_comprehension

async def measure_runtime() -> float:
    """
    measure_runtime - Measures total runtime of async_comprehension.

    This coroutine executes async_comprehension four times in parallel using
    asyncio.gather(), measures the total runtime, and returns it.

    Returns:
        float: Total runtime in seconds.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_time = time.perf_counter() - start_time
    return total_time

# Example usage
async def main():
    print(await measure_runtime())

if __name__ == "__main__":
    asyncio.run(main())
