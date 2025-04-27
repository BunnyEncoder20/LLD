from colorama import Fore, Back, Style

from vehicle_type import VehicleType
from vehicle import Vehicle

class ParkingSpot:
    def __init__(self, spot_num: int):
        self._id = spot_num
        self.spots_vehicle_type = VehicleType.CAR # default spot type is car
        self.parked_vehicle = None
    
    # getters
    def get_id(self): return self._id
    def get_spots_vehicle_type(self) -> VehicleType: return self.spots_vehicle_type
    def get_parked_vehicle(self) -> Vehicle:
        if self.parked_vehicle: return self.parked_vehicle
        else: return None
    
    def isAvailable(self) -> bool:
        return self.parked_vehicle is None
    
    def park_vehicle(self, vehicle: Vehicle) -> None:
        self.parked_vehicle = vehicle
        print(f"{Vehicle} parked.")
        return
    
    def unpark_vehicle(self) -> None:
        self.parked_vehicle = None
        print(f"{self._id} is now empty.")
        return
         
            