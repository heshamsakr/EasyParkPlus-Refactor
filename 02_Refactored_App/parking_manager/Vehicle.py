from abc import ABC, abstractmethod

#Vehicle class for use with Parking Lot Manager
#Set Vehicle an abstract class
class Vehicle(ABC):
    def __init__(self,regNum,make,model,color): #Rename regnum -> regNum
        self._validate_parameters(regNum,make,model,color)
        self._color = color
        self._regNum = regNum
        self._make = make
        self._model = model

    #Validate vehicle parameters.
    @staticmethod
    def _validate_parameters(regNum,make,model,color):
        if not all([regNum,make,model,color]):
            raise ValueError("All vehicle parameters must be non-empty")

        if not all(isinstance(param, str) for param in [regNum,make,model,color]):
            raise ValueError("All vehicle parameters must be strings")

    #Use property instead of get methods
    @property
    def make(self):
        return self._make

    @property
    def model(self):
        return self._model

    @property
    def color(self):
        return self._color

    @property
    def regNum(self):
        return self._regNum

    @abstractmethod
    def getType(self): #Set the getType() method an abtractmethod
        pass

    def __str__(self):
        """String representation of vehicle."""
        return (f"{self.getType()}: {self.make} {self.model} "
                f"({self.color}) - {self.regNum}")

#Car, Truck, Motocycle, Bus classes inherit from Vehicle
class Car(Vehicle):
    def __init__(self,regNum,make,model,color):
        super().__init__(regNum,make,model,color)

    def getType(self):
        return "Car"

class Truck(Vehicle):
    def __init__(self,regNum,make,model,color):
        super().__init__(regNum,make,model,color)

    def getType(self):
        return "Truck"


class Motorcycle(Vehicle):
    def __init__(self,regNum,make,model,color):
        super().__init__(regNum,make,model,color)

    def getType(self):
        return "Motorcycle"

class Bus(Vehicle):
    def __init__(self,regNum,make,model,color):
        super().__init__(regNum,make,model,color)

    def getType(self):
        return "Bus"

#ElectricVehicle inherit from Vehicle
class ElectricVehicle(Vehicle):
    def __init__(self,regNum,make,model,color,charge = 0):
        super().__init__(regNum,make,model,color)
        self._validate_charge(charge)
        self._charge = charge

    #Validate the charge value
    @staticmethod
    def _validate_charge(charge):
        if not (0 <= charge <= 100):
            raise ValueError("Charge must be between 0 and 100%")

    @property
    def charge(self):
        return self._charge

    @charge.setter
    def charge(self,chargeValue):
        self._validate_charge(chargeValue)
        self._charge = chargeValue

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} [Charge: {self.charge}%]"

#ElectricCar & ElectricBike inherit from ElectricVehicle
class ElectricCar(ElectricVehicle):
    def __init__(self,regNum,make,model,color,charge):
        super().__init__(regNum,make,model,color,charge)

    def getType(self):
        return "Electric Car" #Correct type return

class ElectricBike(ElectricVehicle):
    def __init__(self,regNum,make,model,color,charge):
        super().__init__(regNum,make,model,color,charge)

    def getType(self):
        return "Electric Bike" #Correct type return

