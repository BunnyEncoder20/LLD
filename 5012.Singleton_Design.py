import threading

class Logger():
    # private attributes
    __lock = threading.Lock()
    __instance = None
    
    
    def __new__(cls):
        # double checking lock (cause locks are expensive)
        if not cls.__instance:
            with cls.__lock:
                if not cls.__instance:
                    print("Making Logger instance...⭕")
                    
                    # sending cls to Object class (which is the parent)
                    # to make a object of the class cls
                    cls.__instance = super().__new__(cls)
        return cls.__instance
    
    # public 
    def log(self, e, msg):
        print(f"[{e}]: {msg}")

l1 = Logger()
l2 = Logger()

# check if same instance
print(l1 is l2)

l1.log("l1", "Hello, Is the logger working?")
l2.log("l2", "Wordl, Yes it is working fine.")