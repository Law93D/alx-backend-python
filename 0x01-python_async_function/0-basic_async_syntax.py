#!/usr/bin/env python3
import asyncio
import random
from typing import Union

async def wait_random(max_delay: int = 10) -> Union[float, int]:
    """
    Waits for a random delay between 0 and max_delay seconds and returns the delay.

    Args:
        max_delay (int): Maximum delay in seconds.

    Returns:
        float: Random delay between 0 and max_delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
