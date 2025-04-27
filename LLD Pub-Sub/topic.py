class Topic:
    def __init__(self, name):
        self.name = name
        self.subscribers = set()
    
    def get_name(self):
        return self.name
    
    def add_subscriber(self, subscriber):
        self.subscribers.add(subscriber)
    
    def remove_subscriber(self, subscriber):
        self.subscribers.discard(subscriber)
    
    def publish(self, message):
        for sub in self.subscribers:
            sub.on_message(message)