from console_subscriber import ConsoleSubscriber
from message import Message 
from publisher import Publisher
from pub_sub_system import PubSubSystem

class PubSubSystem_Demo:
    @staticmethod
    def run():
        # create system instance
        pub_sub_system = PubSubSystem()

        # create topics
        pub_sub_system.create_topic("Bikes")
        pub_sub_system.create_topic("Cars")
        pub_sub_system.create_topic("Pizza")
        
        # Create subscribers
        subscriber1 = ConsoleSubscriber("Subscriber1")
        subscriber2 = ConsoleSubscriber("Subscriber2")
        subscriber3 = ConsoleSubscriber("Subscriber3")

        # Subscriber to topics
        pub_sub_system.subscribe("Bikes", subscriber1)
        pub_sub_system.subscribe("Cars", subscriber1)
        pub_sub_system.subscribe("Cars", subscriber2)
        pub_sub_system.subscribe("Pizza", subscriber2)
        pub_sub_system.subscribe("Bikes", subscriber3)
        pub_sub_system.subscribe("Cars", subscriber3)
        pub_sub_system.subscribe("Pizza", subscriber3)
        
        # Create Publishers
        pub1 = Publisher(pub_sub_system.get_topics().get("Bikes"))
        pub2 = Publisher(pub_sub_system.get_topics().get("Cars"))
        pub3 = Publisher(pub_sub_system.get_topics().get("Pizza"))

        # Publish Messages
        pub1.publish(Message("Honda CBR650r is a really good sports bike"))
        pub2.publish(Message("Lamborgini Urus is most suitable super car for Indian roads"))
        pub3.publish(Message("Margarita Pizza actual is just base + sause + chesse"))
        
        # Unsubscribe 
        pub_sub_system.unsubscribe("Cars", subscriber1)
        pub_sub_system.unsubscribe("Cars", subscriber2)
        
        # Publish more messages
        pub1.publish(Message("Hero Xpulse seems most comfortable bikes for indian roads"))
        pub2.publish(Message("Chinese cars are insanly good. Especially EVs"))
        pub3.publish(Message("American State Type Pizza's (Detroit/Chicago) have cheese under the sause"))

        # shutdown the system 
        pub_sub_system.shutdown()
        
if __name__ == "__main__":
    PubSubSystem_Demo.run()