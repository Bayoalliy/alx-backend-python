#!/usr/bin/env python3
"""
Import async_comprehension from the previous file and write
a measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather.

measure_runtime should measure the total runtime and return it.
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """mwasures running time of async_comprehension"""
    start_time: float = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    finish_time: float = time.perf_counter()

    return finish_time - start_time
