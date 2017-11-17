import logging

''' Instructions:
DEBUG: Detailed information, typically for interest when diagnosing problems
INFO: Confirmation that things are working as expected
WARNING: An indication that something unexpected happened, or indicative of some problem
        in the near future (e.g: disk_space_low). The software is still working as expected
ERROR: Due to a more serious problem, the software has not been able to perform some function
CRITICAL: A serious error, indicating that the program itself may be unable to continue running
'''


class PaLogger:
    def __init__(self, logger_name, path, filename, level="DEBUG", debug=True):
        self.logger = logging.getLogger(logger_name)
        self.set_logger_level(level)
        self.formatter = logging.Formatter("%(levelname)s:"
                                           "%(asctime)s -- "
                                           "calls from [%(name)s]:"
                                           "%(message)s",
                                           datefmt='%d/%m/%Y %I:%M:%S %p')
        self.file_handler = PaFileHandler(path, filename)
        self.file_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handler)
        if debug:
            self.ch = logging.StreamHandler()
            if level == "DEBUG":
                self.ch.setLevel(logging.DEBUG)
            elif level == "INFO":
                self.ch.setLevel(logging.INFO)
            elif level == "WARNING":
                self.ch.setLevel(logging.WARNING)
            elif level == "ERROR":
                self.ch.setLevel(logging.ERROR)
            elif level == "CRITICAL":
                self.ch.setLevel(logging.CRITICAL)
            self.ch.setFormatter(self.formatter)
            self.logger.addHandler(self.ch)
        super(PaLogger, self).__init__()

    def log(self, msg):
        # TODO: Try a function and then output the log
        self.logger.debug(msg)

    def set_logger_level(self, level):
        if level == "DEBUG":
            self.logger.setLevel(logging.DEBUG)
        elif level == "INFO":
            self.logger.setLevel(logging.INFO)
        elif level == "WARNING":
            self.logger.setLevel(logging.WARNING)
        elif level == "ERROR":
            self.logger.setLevel(logging.ERROR)
        elif level == "CRITICAL":
            self.logger.setLevel(logging.CRITICAL)


class PaFileHandler(logging.FileHandler):
    def __init__(self, path, filename, mode="a"):
        super(PaFileHandler, self).__init__(path + "/" + filename, mode)
