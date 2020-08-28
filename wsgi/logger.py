"""
Logger Class that can be used in any of your application modules
"""

import logging
import datetime
import os
from functools import wraps
import time


class Logger(object):
    """
        Defines a logger instantiated with logger name and format.
    """

    def __init__(self, logger_name, log_level=logging.DEBUG,
                 format="[%(name)s] [%(pathname)s:%(funcName)s():%(lineno)d] [%(levelname)s] %(message)s"):
        self.log_level = log_level
        self.format = format
        self.logger_name = logger_name
        self.logger_obj = logging.getLogger(logger_name)
        self.logger_obj.setLevel(log_level)

    def __repr__(self):
        return "Logger('{}')".format(self.logger_name)

    @property
    def app_logger_obj(self):
        return self.logger_obj

    @app_logger_obj.setter
    def app_logger_obj(self, log_dir):
        stream_format = logging.Formatter(self.format)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(stream_format)
        stream_handler.setLevel(logging.INFO)
        self.logger_obj.addHandler(stream_handler)
        if os.path.isdir(log_dir):
            file_format = logging.Formatter(
                "[%(asctime)s] [%(name)s] [%(pathname)s:%(funcName)s():%(lineno)d] [%(levelname)s] %(message)s",
                datefmt="%A %d-%b-%Y %I:%M:%S %p")
            file_name = "{}_{}.log".format(self.logger_name, datetime.datetime.today().strftime("%d%b%Y"))
            file_path = os.path.join(log_dir, file_name)
            file_handler = logging.FileHandler(file_path)
            file_handler.setFormatter(file_format)
            file_handler.setLevel(logging.DEBUG)
            self.logger_obj.addHandler(file_handler)
        else:
            self.logger_obj.warn("File Logging Couldn't be enabled as the path %s is not a valid directory", log_dir)
            self.logger_obj.info("Only Console Logging enabled")

    @app_logger_obj.deleter
    def app_logger_obj(self):
        del self.logger_obj

    def log_func_time(self, func):
        @wraps(func)
        def wrapper_time(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            self.logger_obj.debug(
                "Called function '{}' with args '{}' took time '{}' s".format(func.__name__, (args, kwargs),
                                                                              end - start))
            return result

        return wrapper_time


logger_obj = Logger("my_logger")
logger_obj.app_logger_obj = os.path.join(os.path.abspath(os.path.curdir), "logs")
app_logger = logger_obj.app_logger_obj
