from log_appender import LogAppender

class FileAppender(LogAppender):
    def __init__(self, filePath):
        self.filePath = filePath
        
    def append(self, log_message):
        with open(self.filePath, "a") as file:
            file.write(str(log_message)+"\n")