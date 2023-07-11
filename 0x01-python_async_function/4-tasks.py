#!/usr/bin/env python3
"""
execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    returns a list of floats
    """
    list_delay = []
    for _ in range(n):
        value = await task_wait_random(max_delay)
        list_delay.append(value)
    return sorted(list_delay)
