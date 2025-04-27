from uuid import uuid4
from abc import ABC, abstractmethod

# observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, message): pass

# concrete class 
class User(Observer):
    def __init__(self, username):
        self.__uid = uuid4()
        self._username = username

    def update(self, msg):
        print(f"[{self.__uid}:{self._username}] received msg: {msg}")

# subject Interface
class Subject(ABC):
    @abstractmethod
    def subscribe(self, observer: Observer): pass
    
    @abstractmethod
    def unsubscribe(self, observer: Observer): pass
    
    @abstractmethod
    def notify(self, msg: str): pass

# concrete subject
class Group(Subject):
    def __init__(self):
        self.__observers = []
    
    def subscribe(self, new_observer: Observer):
        self.__observers.append(new_observer)
    
    def unsubscribe(self, observer: Observer):
        self.__observers.remove(observer)
    
    def notify(self, msg: str):
        print("Notifying group members:")
        for user in self.__observers:
            user.update(msg)


if __name__ == "__main__":
    friend_group = Group()

    bunny = User("Bunny")
    soma = User("Soma")
    bunnu = User("Bunnu")
    hooda = User("Hooda")
    tarun = User("Tarun")

    friend_group.subscribe(bunny)
    friend_group.subscribe(soma)
    friend_group.subscribe(bunnu)
    friend_group.subscribe(hooda)
    friend_group.subscribe(tarun)

    friend_group.notify("Group created successfully 🎉")
    friend_group.notify("Hello Hello Hello, welcome to the group !")

    friend_group.unsubscribe(tarun)
    friend_group.notify("Tarun has left the group 😢")
