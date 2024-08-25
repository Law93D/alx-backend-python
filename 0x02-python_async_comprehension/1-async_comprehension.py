#!/usr/bin/env python3
"""Task 1's module"""
from importlib import import_module as using
import asyncio
from typing import List


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers using async comprehending over async_generator."""
    return [num async for num in async_generator()]
