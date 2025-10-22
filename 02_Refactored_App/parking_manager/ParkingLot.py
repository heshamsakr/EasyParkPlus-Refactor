from .Vehicle import Vehicle, ElectricVehicle

### DESIGN PATTERN: OBSERVER PATTERN (GoF Behavioral Pattern)
class ParkingObserver:
    """Observer interface for Observer Pattern"""
    def update(self, message):
        """Called when parking lot state changes"""
        pass  # To be implemented by concrete observers

class ParkingLot:
    """ParkingLot class - manages vehicle parking"""

    def __init__(self):
        """Initialize empty parking lot"""
        self.capacity = 0
        self.evCapacity = 0
        self.level = 0
        self.slotId = 0 # Rename slotid -> slotId
        self.slotEvId = 0
        self.numOfOccupiedSlots = 0
        self.numOfOccupiedEvSlots = 0

        # Observer pattern: list of observers to notify
        self.observers = []

    # Observer Pattern methods
    def attachObserver(self, observer):
        """
        Register an observer to receive updates

        Args:
            observer: Object implementing ParkingObserver interface
        """
        if observer not in self.observers:
            self.observers.append(observer)

    def detachObserver(self, observer):
        """Remove an observer"""
        if observer in self.observers:
            self.observers.remove(observer)

    def notifyObservers(self, message):
        """
        Notify all observers of a change

        Args:
            message: What changed in the parking lot
        """
        for observer in self.observers:
            observer.update(message)

    def createParkingLot(self, capacity, evCapacity, level):
        """
        Create parking lot with specified capacity

        IMPROVEMENT: Uses None instead of -1 for empty slots
        """
        self.capacity = capacity
        self.evCapacity = evCapacity
        self.level = level

        # None is clearer than -1 for "empty slot"
        self.slots = [None] * capacity
        self.evSlots = [None] * evCapacity

        return self.level

    def getEmptySlot(self):
        """Find first empty regular slot"""
        for i in range(len(self.slots)):
            if self.slots[i] is None:  # Clearer than == -1
                return i
        return None

    def getEmptyEvSlot(self):
        """Find first empty EV slot"""
        for i in range(len(self.evSlots)):
            if self.evSlots[i] is None:  # Clearer than == -1
                return i
        return None

    def park(self, vehicle, isElectric=False):
        """
        Park a vehicle in appropriate slot

        IMPROVEMENTS:
        1. Takes vehicle object instead of separate parameters
        2. Uses boolean isElectric instead of magic number (ev=1)
        3. Notifies observers instead of directly updating GUI

        Args:
            vehicle: Vehicle object to park
            isElectric: True if electric vehicle, False otherwise

        Returns:
            Slot number if successful, None if lot is full
        """
        # Check if electric vehicle
        if isElectric:
            # Check EV capacity
            if self.numOfOccupiedEvSlots < self.evCapacity:
                slotIndex = self.getEmptyEvSlot()

                if slotIndex is not None:
                    # Park the vehicle
                    self.evSlots[slotIndex] = vehicle
                    self.slotEvId += 1
                    self.numOfOccupiedEvSlots += 1

                    # Notify observers (instead of directly updating GUI)
                    self.notifyObservers(
                        f"Vehicle {vehicle.regNum} parked "
                        f"in EV slot {self.slotEvId}"
                    )

                    return self.slotEvId

        # Regular vehicle
        else:
            # Check regular capacity
            if self.numOfOccupiedSlots < self.capacity:
                slotIndex = self.getEmptySlot()

                if slotIndex is not None:
                    # Park the vehicle
                    self.slots[slotIndex] = vehicle
                    self.slotId += 1
                    self.numOfOccupiedSlots += 1

                    # Notify observers (instead of directly updating GUI)
                    self.notifyObservers(
                        f"Vehicle {vehicle.regNum} parked "
                        f"in regular slot {self.slotId}"
                    )

                    return self.slotId

        # Lot is full
        return None

    def leave(self, slotNumber, isElectric=False):
        """
        Remove vehicle from slot

        IMPROVEMENT: Uses boolean isElectric instead of magic number

        Args:
            slotNumber: Slot to clear (1-indexed)
            isElectric: True if EV slot, False if regular

        Returns:
            True if successful, False if slot was empty
        """

        if isElectric:
            # EV slot
            if (self.numOfOccupiedEvSlots > 0 and
                    slotNumber <= len(self.evSlots) and
                    self.evSlots[slotNumber - 1] is not None):
                vehicle = self.evSlots[slotNumber - 1]
                self.evSlots[slotNumber - 1] = None
                self.numOfOccupiedEvSlots -= 1

                # Notify observers
                self.notifyObservers(
                    f"Vehicle {vehicle.regNum} removed "
                    f"from EV slot {slotNumber}"
                )

                return True
        else:
            # Regular slot
            if (self.numOfOccupiedSlots > 0 and
                    slotNumber <= len(self.slots) and
                    self.slots[slotNumber - 1] is not None):
                vehicle = self.slots[slotNumber - 1]
                self.slots[slotNumber - 1] = None
                self.numOfOccupiedSlots -= 1

                # Notify observers
                self.notifyObservers(
                    f"Vehicle {vehicle.regNum} removed "
                    f"from regular slot {slotNumber}"
                )

                return True

        return False

    def getStatus(self):
        """
        Get current parking lot status

        IMPROVEMENT: Returns data instead of directly updating GUI
        This allows Observer to handle display

        Returns:
            Dictionary with regular and EV vehicle lists
        """
        status = {
            'regular': [],
            'electric': []
        }

        # Get regular vehicles
        for i, vehicle in enumerate(self.slots):
            if vehicle:
                status['regular'].append({
                    'slot': i + 1,
                    'level': self.level,
                    'registration': vehicle.regNum,
                    'color': vehicle.color,
                    'make': vehicle.make,
                    'model': vehicle.model
                })

        # Get EV vehicles
        for i, eVehicle in enumerate(self.evSlots):
            if eVehicle:
                status['electric'].append({
                    'slot': i + 1,
                    'level': self.level,
                    'registration': eVehicle.regNum,
                    'color': eVehicle.color,
                    'make': eVehicle.make,
                    'model': eVehicle.model,
                    'charge': eVehicle.charge if isinstance(eVehicle, ElectricVehicle) else 0
                })

        return status

    def findByRegNum(self, regNum):
        """
        Find vehicle by registration number

        Returns:
            Tuple of (slotNumber, isElectric) or None if not found
        """
        # Search regular slots
        for i, vehicle in enumerate(self.slots):
            if (vehicle is not None and vehicle.regNum == regNum):
                return (i + 1, False)

        # Search EV slots
        for i, eVehicle in enumerate(self.evSlots):
            if (eVehicle is not None and eVehicle.regNum == regNum):
                return (i + 1, True)

        return None

    def findByColor(self, color):
        """
        Find all vehicles of a specific color

        Returns:
            List of tuples: (slotNumber, isElectric)
        """
        results = []

        # Search regular slots
        for i, vehicle in enumerate(self.slots):
            if (vehicle is not None and vehicle.color.lower() == color.lower()):
                results.append((i + 1, False))

        # Search EV slots
        for i, eVehicle in enumerate(self.evSlots):
            if (eVehicle is not None and eVehicle.color.lower() == color.lower()):
                results.append((i + 1, True))

        return results

    # Remove other unused functions
