from concurrent.futures import ThreadPoolExecutor
from topic import Topic

class PubSubSystem:
    def __init__(self):
        self.topics = {}
        # multithreading
        self.executor_service = ThreadPoolExecutor(max_workers=10)
    
    def get_topics(self):
        return self.topics
    
    def create_topic(self, topic_name):
        self.topics.setdefault(topic_name, Topic(topic_name))
        print(f"[Pub-Sub]: {topic_name} Topic created")

    def subscribe(self, topic_name, subscriber):
        topic = self.topics.get(topic_name)
        if topic:
            topic.add_subscriber(subscriber)
            print(f"[Pub-Sub]: {subscriber} subbed to {topic_name} Topic")

        
    def unsubscribe(self, topic_name, subscriber):
        topic = self.topics.get(topic_name)
        if topic:
            topic.remove_subscriber(subscriber)
            print(f"[Pub-Sub]: {subscriber} unsubscribed from {topic_name} Topic")
    
    def publish(self, topic_name, message):
        topic = self.topics.get(topic_name)
        if topic:
            self.executor_service.submit(topic.publish, message)

    
    def shutdown(self):
        self.executor_service.shutdown()
        print(f"[Pub-Sub]: System Shutdown.")

    
    