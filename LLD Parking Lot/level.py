from typing import List 
from parking_spot import ParkingSpot
from vehicle import Vehicle

from colorama import init, Fore, Back, Style
init(autoreset=True)    # resets the styling after every print line

class Level:
    def __init__(self, floor: int, num_spots: int):
        self._id = floor
        self.parking_spots: List[ParkingSpot] = [ParkingSpot(i) for i in range(1,num_spots+1)]
    
    def park_vehicle(self, vehicle: Vehicle) -> bool:
        for spot in self.parking_spots:
            if spot.isAvailable() and spot.get_spots_vehicle_type() == vehicle.get_type():
                spot.park_vehicle(vehicle)
                print(f"[Level]: parked {vehicle} at {self._id}-{spot._id}")
                return True
        return False
    
    def unpark_vehicle(self, vehicle: Vehicle) -> bool:
        for spot in self.parking_spots:
            if not spot.isAvailable() and spot.get_parked_vehicle() == vehicle:
                spot.unpark_vehicle()
                print(f"[Level]: {vehicle} left parking {self._id}-{spot._id}")
                return True
        return False
    
    def getAvailabilityReport(self) -> str:
        print(Fore.WHITE + f"Level {self._id} Availability:")
        for spot in self.parking_spots:
            if spot.isAvailable():
                print(Fore.WHITE + f"Spot {spot.get_id()} is "+ Back.GREEN +"AVAILABLE")
            else:
                print(Fore.WHITE + f"Spot {spot.get_id()} is "+ Back.RED +"NOT AVAILABLE")
        print(Style.RESET_ALL)
                