#!/usr/bin/env python3
"""
2-measure_runtime.py - Measures runtime of async_comprehension in parallel.

This module measures the total runtime of executing async_comprehension four
times in parallel using asyncio.gather().
"""

import asyncio
import time
from typing import List
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the total runtime for executing async_comprehension four times in parallel."""
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time - start_time
