'''Tornado ioloop.py 源码学习

# 知识图谱
- __future__
- 库包
    - collections
    - errno
    - functools
    - heapq
    - itertools
    - numbers
    - os
    - select
    - threading
    - traceback
    - math
    - signal
    - concurrent
    - asyncio
- 文件描述符
- select
- epoll
- kqueue

# 参考
'''


__author__ = 'happyin3 (happyinx3@gmail.com)'


class IOLoop(Configurable):
    @classmethod
    def configure(cls, impl, **kwargs):
        pass

    @staticmethod
    def instance():
        pass

    def install(self):
        pass

    @staticmethod
    def clear_instance():
        pass

    @staticmethod
    def current(instance=True):
        pass

    def make_current(self):
        pass

    @staticmethod
    def clear_current():
        pass

    def _clear_current_hook(self):
        pass

    @classmethod
    def configurable_base(cls):
        pass

    @classmethod
    def configurable_default(cls):
        pass

    def initialize(self, make_current=None):
        pass

    def close(self, all_fds=False):
        pass

    def add_handler(self, fd, handler, events):
        pass

    def update_handler(self, fd, events):
        pass

    def remove_handler(self, fd):
        pass

    def set_blocking_signal_threshold(self, seconds, action):
        pass

    def set_blocking_log_threshold(self, seconds):
        pass

    def log_stack(self, signal, frame):
        pass

    def start(self):
        pass

    def _setup_logging(self):
        pass

    def stop(self):
        pass

    def run_sync(self, func, timeout=None):
        def run():
            pass
        pass

    def time(self):
        pass

    def add_timeout(self, deadline, callback, *args, **kwargs):
        pass

    def call_later(self, delay, callback, *args, **kwargs):
        pass

    def call_at(self, when, callback, *args, **kwargs):
        pass

    def remove_timeout(self, timeout):
        pass

    def add_callback(self, callback, *args, **kwargs):
        pass

    def add_callback_from_signal(self, callback, *args, **kwargs):
        pass

    def spawn_callback(self, callback, *args, **kwargs):
        pass

    def add_future(self, future, callback):
        pass

    def run_in_executor(self, executor, func, *args):
        pass

    def set_default_executor(self, executor):
        pass

    def _run_callback(self, callback):
        pass

    def _discard_future_result(self, future):
        pass

    def handle_callback_exception(self, callback):
        pass

    def split_fd(self, fd):
        pass

    def close_fd(self, fd):
        pass


class PollIOLoop(IOLoop):
    def initialize(self, impl, time_func=None, **kwargs):
        pass

    @classmethod
    def configurable_base(cls):
        pass

    @classmethod
    def configurable_default(cls):
        pass

    def close(self, all_fds=False):
        pass

    def add_handler(self, fd, handler, events):
        pass

    def update_handler(self, fd, events):
        pass

    def remove_handler(self, fd):
        pass

    def set_blocking_signal_threshold(self, seconds, action):
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def time(self):
        pass

    def call_at(self, deadline, callback, *args, **kwargs):
        pass

    def remove_timeout(self, timeout):
        pass

    def add_callback(self, callback, *args, **kwargs):
        pass

    def add_callback_from_signal(self, callback, *args, **kwargs):
        pass


class _Timeout(object):
    def __init__(self, deadline, callback, io_loop):
        pass

    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass


class PeriodicCallback(object):
    def __init__(self, callback, callback_time, jitter=0):
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def is_running(self):
        pass

    def _run(self):
        pass

    def _schedule_next(self):
        pass

    def _update_next(self, current_time):
        pass
