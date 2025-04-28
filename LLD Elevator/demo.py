import time 
from elevator_controller import ElevatorController

class ElevatorSystem_demo:
    @staticmethod
    def run():
        controller = ElevatorController(3,5)
        time.sleep(3)
        controller.request_elevator(10,12)
        time.sleep(3)
        controller.request_elevator(1,7)
        time.sleep(3)
        controller.request_elevator(2,5)
        time.sleep(3)
        controller.request_elevator(1,9)
        
        # keep the main thread running 
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Elevator system stopped")

if __name__ == "__main__":
    ElevatorSystem_demo.run()