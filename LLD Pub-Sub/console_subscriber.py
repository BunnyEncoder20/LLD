from subscriber import Subscriber

class ConsoleSubscriber(Subscriber):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
    
    def on_message(self, message):
        print(f"Subscriber {self.name} received message: {message.get_content()}")