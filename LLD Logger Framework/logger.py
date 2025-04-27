from logger_config import LoggerConfig
from log_level import LogLevel
from log_message import LogMessage
from console_appender import ConsoleAppender

class Logger:
    _instance = None
    
    def __init__(self):
        if Logger._instance is not None:
           raise Exception("Logger is singleton!") 
        else:
            Logger._instance = self
            self.config = LoggerConfig(LogLevel.INFO, ConsoleAppender())
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            Logger()
        return cls._instance

    def set_config(self, config):
        self.config = config
    
    def log(self, level, message):
        if level.value >= self.config.get_log_level().value:
            log_msg = LogMessage(level, message)
            self.config.get_log_appender().append(log_msg)
        
    def debug(self, message):
        self.log(LogLevel.DEBUG, message)
    
    def info(self, message):
        self.log(LogLevel.INFO, message)
    
    def warning(self, message):
        self.log(LogLevel.WARNING, message)
    
    def error(self, message):
        self.log(LogLevel.ERROR, message)
    
    def fatal(self, message):
        self.log(LogLevel.FATAL, message)