import logging
# import logging.config
# logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=False)


class ParabankLogger:

    def __init__(self, filename):
        # Create a custom logger
        # logging.basicConfig(format='%(message)s', level=logging.INFO, force=True)
        # self.logger = logging.getLogger(__name__)
        self.logger = logging.getLogger('parabank_logger')
        self.logger.setLevel(logging.INFO)
        # Create handler
        self.handler = logging.FileHandler(filename)
        self.handler.setLevel(logging.INFO)
        # Create formatter and add it to handlers
        # self.logger_format = logging.Formatter('%(module)s - %(funcName)s - %(message)s')
        self.logger_format = logging.Formatter('%(message)s')
        self.handler.setFormatter(self.logger_format)
        # Add handler to the logger
        if not self.logger.handlers:
            self.logger.addHandler(self.handler)
        # self.logger.propagate = False
