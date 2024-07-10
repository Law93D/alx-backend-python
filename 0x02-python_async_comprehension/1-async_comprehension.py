#!/usr/bin/env python3
import asyncio
from typing import List
from async_generator import async_generator

async def async_comprehension() -> List[float]:
    """Collects 10 random numbers using async comprehending over async_generator."""
    return [num async for num in async_generator()]
