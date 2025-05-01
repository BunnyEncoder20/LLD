import time 
from threading import Lock, Condition
from request import Request
from direction import Direction

class Elevator:
    def __init__(self, id: int, cap: int):
        self._id = id
        self._capacity = cap
        self.current_floor = 1
        self.current_direction = Direction.UP
        self.requests = []
        self.lock = Lock()
        self.condition = Condition(self.lock)
    
    def add_request(self, request: Request):
        with self.lock:
            if len(self.requests) < self._capacity:
                self.requests.append(request)
                print(f"Elevator {self._id} added request: {request.source_floor} to {request.destination_floor}")
                self.condition.notify_all()
    
    def get_next_request(self) -> Request:
        with self.lock:
            while not self.requests:
                self.condition.wait()
            return self.requests.pop(0)
    
    def process_requests(self):
        while True:
            request = self.get_next_request()
            self.process_request(request)
    
    def process_request(self, request: Request):
        start_floor = self.current_floor
        end_floor = request.destination_floor
        
        if start_floor < end_floor:
            self.current_direction = Direction.UP
            for i in range(start_floor, end_floor - 1, -1):
                self.current_floor = i
                print(f"Elevator {self._idid} reached floor {self.current_floor}")
                time.sleep(1) # simulating physical elevator moving from floor to floor
        
        elif start_floor > end_floor:
            self.current_direction = Direction.DOWN
            for i in range(start_floor, end_floor-1, -1):
                self.current_floor = i
                print(f"Elevator {self._idid} reached floor {self.current_floor}")
                time.sleep(1)
    
    def run(self):
        self.process_requests()

