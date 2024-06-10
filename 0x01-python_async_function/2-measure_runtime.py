#!/usr/bin/env python3
"""Measures  runtime"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Returns total execution time
    divided by n (float)"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    runtime = end_time - start_time
    return runtime / n
