#!/usr/bin/env python3
"""write an async routine called wait_n that takes in 2 int 
arguments (in this order): n and max_delay.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times"""
    tasks = []
    delays = []

    i = 0
    while i <- n:
        task = wait_random(max_delay)
        tasks.append(task)
        i += 1

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delays
