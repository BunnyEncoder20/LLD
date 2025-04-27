from typing import List 
from level import Level
from vehicle import Vehicle

class ParkingLot:
    _instance = None
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def __init__(self):
        if self._instance is not None:
            raise Exception("[ERROR]:ParkingLot.__init__():Parking Lot can only have one instance !")
        else:
            # assigning singleton instance
            self._instance = self
            
            # list of levles, of type Level class
            self.levels: List[Level] = []
    
    
    # instance methods
    def add_level(self, lvl: Level) -> None:
        self.levels.append(lvl)
        print("[ParkingLot]: Level added successfully")
        return
    
    def park_vehicle(self, vehicle: Vehicle) -> bool:
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True
        return False

    def unpark_vehicle(self, vehicle: Vehicle) -> bool:
        for level in self.levels:
            if level.unpark_vehicle(vehicle):
                return True
        return False
    
    def display_availability(self) -> None:
        for level in self.levels:
            level.getAvailabilityReport()
        return