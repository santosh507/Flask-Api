"""
Logger Class that can be used in any of your application modules
"""

import logging
import datetime
import os


class Logger(object):
    """
        Defines a logger instantiated with logger name and format.
    """

    def __init__(self, logger_name, log_level=logging.INFO,
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
        stream_format = logging.Formatter(self.format)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(stream_format)
        stream_handler.setLevel(self.log_level)
        file_format = logging.Formatter(
            "[%(asctime)s] [%(name)s] [%(pathname)s:%(funcName)s():%(lineno)d] [%(levelname)s] %(message)s")
        file_name = "{}_{}.log".format(self.logger_name, datetime.datetime.today().strftime("%d%m%Y"))
        abs_path = os.path.abspath(".")
        file_path = os.path.join(abs_path, "logs", file_name)
        file_handler = logging.FileHandler(file_path)
        file_handler.setFormatter(file_format)
        file_handler.setLevel(logging.DEBUG)
        self.logger_obj.addHandler(stream_handler)
        self.logger_obj.addHandler(file_handler)
        self.logger_obj.setLevel(logging.DEBUG)
        return self.logger_obj

    @app_logger_obj.setter
    def app_logger_obj(self, log_obj):
        self.logger_obj = log_obj

    @app_logger_obj.deleter
    def app_logger_obj(self):
        del self.logger_obj
