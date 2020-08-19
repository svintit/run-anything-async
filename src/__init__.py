"""
USAGE:

    @async_no_await
    def greeting():
        # Do some long, complicated task
        print("Hello World")

    greeting()

"""

import asyncio


def async_no_await(func):
    def decorator(*args, **kwargs):
        return asyncio.get_event_loop().run_in_executor(None, func, *args)

    return decorator
