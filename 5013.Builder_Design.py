from abc import ABC, abstractmethod 

# Product class
class Desktop():
    def __init__(self):
        self._monitor = None
        self._keyboard = None
        self._mouse = None
        self._speaker = None
        self._ram = None
        self._processor = None
        self._motherBoard = None

    def setMonitor(self, monitor): self._monitor = monitor
    def setKeyboard(self, keyboard): self._keyboard = keyboard
    def setMouse(self, mouse): self._mouse = mouse
    def setSpeaker(self, speaker): self._speaker = speaker
    def setRam(self, ram): self._ram = ram
    def setProcessor(self, processor): self._processor = processor
    def setMotherBoard(self, mb): self._motherBoard = mb

    def showSpecs(self):
        print("------------------------------------------")
        print("📋 Desktop Specs:")
        print(f"Monitor: {self._monitor}")
        print(f"Keyboard: {self._keyboard}")
        print(f"Mouse: {self._mouse}")
        print(f"Speaker: {self._speaker}")
        print(f"RAM: {self._ram}")
        print(f"Processor: {self._processor}")
        print(f"MotherBoard: {self._motherBoard}")
        print("------------------------------------------")
        print()

# Abstract Builder
class DesktopBuilder(ABC):
    def __init__(self):
        self._desktop = Desktop()

    @abstractmethod
    def buildMonitor(self): pass

    @abstractmethod
    def buildKeyboard(self): pass

    @abstractmethod
    def buildMouse(self): pass

    @abstractmethod
    def buildSpeaker(self): pass

    @abstractmethod
    def buildRam(self): pass

    @abstractmethod
    def buildProcessor(self): pass

    @abstractmethod
    def buildMotherBoard(self): pass

    def getDesktop(self):
        return self._desktop

# Concrete Builders
class Dell_DesktopBuilder(DesktopBuilder):
    def buildMonitor(self): self._desktop.setMonitor("Dell 24 inch")
    def buildKeyboard(self): self._desktop.setKeyboard("Dell Mechanical")
    def buildMouse(self): self._desktop.setMouse("Dell Wired Mouse")
    def buildSpeaker(self): self._desktop.setSpeaker("Dell Stereo")
    def buildRam(self): self._desktop.setRam("16GB DDR4")
    def buildProcessor(self): self._desktop.setProcessor("Intel i7")
    def buildMotherBoard(self): self._desktop.setMotherBoard("Dell XSeries")

class HP_DesktopBuilder(DesktopBuilder):
    def buildMonitor(self): self._desktop.setMonitor("HP 22 inch")
    def buildKeyboard(self): self._desktop.setKeyboard("HP Wireless")
    def buildMouse(self): self._desktop.setMouse("HP Optical")
    def buildSpeaker(self): self._desktop.setSpeaker("HP SoundBar")
    def buildRam(self): self._desktop.setRam("8GB DDR4")
    def buildProcessor(self): self._desktop.setProcessor("AMD Ryzen 5")
    def buildMotherBoard(self): self._desktop.setMotherBoard("HP B450")

class Asus_DesktopBuilder(DesktopBuilder):
    def buildMonitor(self): self._desktop.setMonitor("Asus Gaming 27 inch")
    def buildKeyboard(self): self._desktop.setKeyboard("Asus RGB Mechanical")
    def buildMouse(self): self._desktop.setMouse("Asus Gaming Mouse")
    def buildSpeaker(self): self._desktop.setSpeaker("Asus Surround Sound")
    def buildRam(self): self._desktop.setRam("32GB DDR5")
    def buildProcessor(self): self._desktop.setProcessor("Intel i9")
    def buildMotherBoard(self): self._desktop.setMotherBoard("Asus ROG Maximus")

# Director
class Director():
    def __init__(self, builder: DesktopBuilder):
        self.__desktop_builder = builder

    def buildDesktop(self):
        self.__desktop_builder.buildMonitor()
        self.__desktop_builder.buildKeyboard()
        self.__desktop_builder.buildMouse()
        self.__desktop_builder.buildSpeaker()
        self.__desktop_builder.buildRam()
        self.__desktop_builder.buildProcessor()
        self.__desktop_builder.buildMotherBoard()
        return self.__desktop_builder.getDesktop()

# Execution
if __name__ == "__main__":
    hp = HP_DesktopBuilder()
    dell = Dell_DesktopBuilder()
    asus = Asus_DesktopBuilder()

    d1 = Director(hp)
    d2 = Director(dell)
    d3 = Director(asus)

    desktop1 = d1.buildDesktop()
    desktop2 = d2.buildDesktop()
    desktop3 = d3.buildDesktop()

    desktop1.showSpecs()
    desktop2.showSpecs()
    desktop3.showSpecs()
