#!/usr/bin/env python3
"""
measure_time function with integers n and max_delay as
arguments that measures the total execution time for wait_n(n, max_delay),
and returns total_time / n. Your function should return a float.

Use the time module to measure an approximate elapsed time
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    returns the total execution time of the function
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total_time = end - start
    return total_time / n
