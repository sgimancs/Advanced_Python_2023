import time

class TimeError(Exception):
    'Exception'

class Timer:

    # CONSTRUCTOR
    def __init__(self):
        self._start_time = None


    # START
    def start(self):
        # """Start a new timer"""
        if self._start_time is not None:
            raise TimeError(f"Timer is running.")

        self._start_time = time.perf_counter()


    # FINISH
    def finish(self):
        #"""Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimeError(f"Timer is running.")

        elapsed_time = time.perf_counter() - self._start_time   # прошедшее время
        self._start_time = None                                 # обнулить таймер
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")
