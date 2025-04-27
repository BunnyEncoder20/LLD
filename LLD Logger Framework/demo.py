from logger import Logger
from logger_config import LoggerConfig
from log_level import LogLevel
from file_appender import FileAppender

class LoggingFramework_Demo:
    @staticmethod
    def run():
        logger = Logger.get_instance()
        
        # Logging with default config
        logger.info('This is an information message')
        logger.warning("This is a warning message")
        logger.error("This is an error message")

        # Changing the log level and appender
        config = LoggerConfig(LogLevel.DEBUG, FileAppender("/Users/varunverma/Code/LeetCode/LLD Logger Framework/app.log"))
        logger.set_config(config)
        
        # Logging with new config 
        logger.debug("This is a debug message")
        logger.info("This is a information message")

if __name__ == "__main__":
    LoggingFramework_Demo.run()
