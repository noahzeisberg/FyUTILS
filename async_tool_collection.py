# All functions here will be later added to the main.py/async.py. This is just because I want the main.py to be clean until the release of the async stuff.
# These functions are providing faster coding, so it's better for me and other developers. If you want to use something in your project, please mention me. :D

import asyncio


def get_threaded_function(func):
    return asyncio.to_thread(func)
