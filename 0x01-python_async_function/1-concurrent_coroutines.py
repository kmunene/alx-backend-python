#!/usr/bin/env python3
"""many coroutines at the same time with async"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_n takes in two int arguments  and returns
    list of total delays in floats
    """
    delays = []
    for _ in range(n):
        delays.append(await wait_random(max_delay))

    return sorted(delays)
