#!/usr/bin/env python3
"""Asynx basics"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Returns a random delay between 0 and maximum
    delay """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
