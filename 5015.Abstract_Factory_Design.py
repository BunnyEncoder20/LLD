from abc import ABC, abstractmethod

# --- Button interface and implementations ---
class IButton(ABC):
    @abstractmethod
    def press(self): pass

class WindowsButton(IButton):
    def press(self):
        print("🪟 Windows Button Pressed!")

class MacButton(IButton):
    def press(self):
        print("🍏 Mac Button Pressed!")

# --- Textarea interface and implementations ---
class ITextarea(ABC):
    @abstractmethod
    def showText(self): pass

class WindowsTextarea(ITextarea):
    def showText(self):
        print("🪟 Windows Textarea Showing Text...")

class MacTextarea(ITextarea):
    def showText(self):
        print("🍏 Mac Textarea Showing Text...")

# --- Abstract Factory ---
class GUI_AbstractFactory(ABC):
    @abstractmethod
    def createButton(self) -> IButton: pass

    @abstractmethod
    def createTextarea(self) -> ITextarea: pass

    @staticmethod
    def createFactory(osType: str):
        if osType.lower() == "windows":
            return WindowsFactory()
        elif osType.lower() == "mac":
            return MacFactory()
        else:
            raise ValueError("❌ Unsupported OS Type!")

# --- Concrete Factories ---
class WindowsFactory(GUI_AbstractFactory):
    def createButton(self) -> IButton:
        return WindowsButton()

    def createTextarea(self) -> ITextarea:
        return WindowsTextarea()

class MacFactory(GUI_AbstractFactory):
    def createButton(self) -> IButton:
        return MacButton()

    def createTextarea(self) -> ITextarea:
        return MacTextarea()


# --- Client side code ---
if __name__ == "__main__":
    osType = input("Enter OS Type (windows / mac): ")

    try:
        # Get the appropriate factory
        factory = GUI_AbstractFactory.createFactory(osType)

        # Create GUI components
        button = factory.createButton()
        textarea = factory.createTextarea()

        # Interact with components
        button.press()
        textarea.showText()

    except ValueError as e:
        print(e)
