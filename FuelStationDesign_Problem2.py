class FuelStation:
    def __init__(self, diesel, petrol, electric):
        # Dictionary to track total slots and occupied slots for each fuel type
        self.fuel_slots = {
            "diesel": {"total": diesel, "occupied": 0},
            "petrol": {"total": petrol, "occupied": 0},
            "electric": {"total": electric, "occupied": 0}
        }
    
    def fuel_vehicle(self, fuel_type):
        # Check if the fuel type exists in our fuel station
        if fuel_type not in self.fuel_slots:
            return False
        
        # Check if there are available slots for this fuel type
        if self.fuel_slots[fuel_type]["occupied"] < self.fuel_slots[fuel_type]["total"]:
            # Occupy a slot
            self.fuel_slots[fuel_type]["occupied"] += 1
            return True
        # No slots available
        return False
    
    def open_fuel_slot(self, fuel_type):
        # Check if the fuel type exists in our fuel station
        if fuel_type not in self.fuel_slots:
            return False
        
        # Check if there are occupied slots to open
        if self.fuel_slots[fuel_type]["occupied"] > 0:
            # Release a slot
            self.fuel_slots[fuel_type]["occupied"] -= 1
            return True
        # No occupied slots to open
        return False

# Test
def test_fuel_station():
    # Create a fuel station with 2 diesel, 2 petrol, and 1 electric slots
    fuel_station = FuelStation(diesel=2, petrol=2, electric=1)
    
    # Test case series
    test_cases = [
        fuel_station.fuel_vehicle("diesel"),     # true (1 slot open)
        fuel_station.fuel_vehicle("petrol"),     # true (1 slot open)
        fuel_station.fuel_vehicle("diesel"),     # true (0 slots open)
        fuel_station.fuel_vehicle("electric"),   # true (0 slots open)
        fuel_station.fuel_vehicle("diesel"),     # false (0 slots open)
        fuel_station.open_fuel_slot("diesel"),   # true (1 slot open)
        fuel_station.fuel_vehicle("diesel"),     # true (0 slots open)
        fuel_station.open_fuel_slot("electric"), # true (1 slot open)
        fuel_station.open_fuel_slot("electric")  # false (only 1 slot available)
    ]


    print(test_cases)

# Run the test
test_fuel_station()
