import tkinter as tk
from tkinter import messagebox
from .Vehicle import VehicleFactory, VehicleType
from .ParkingLot import ParkingLot, ParkingObserver

### Concrete Observer Implementation

class GUIObserver(ParkingObserver):
    """
    Concrete Observer that updates GUI when parking lot changes

    Part of Observer Pattern implementation
    """

    def __init__(self, textWidget):
        """
        Initialize observer with text widget to update

        Args:
            textWidget: Tkinter Text widget to display messages
        """
        self.textWidget = textWidget

    def update(self, message):
        """
        Called by ParkingLot when something changes

        Args:
            message: Status message to display
        """
        self.textWidget.insert(tk.END, message + "\n")
        self.textWidget.see(tk.END)  # Auto-scroll to bottom

# Main GUI Application - Remove global variables
class ParkingManagerGUI:
    """Parking Manager GUI Application"""

    def __init__(self, root):
        """
        Initialize GUI application

        IMPROVEMENT: All variables are instance variables, not globals
        """
        self.root = root
        self.root.geometry("660x850")
        self.root.resizable(True, True) # elf.root.resizable(0, 0) -> self.root.resizable(True, True): Display full content
        self.root.title("Parking Lot Manager - Refactored")

        # Create parking lot instance
        self.parkingLot = ParkingLot()

        # Initialize all GUI variables as instance variables (Not global)
        self.initVariables()

        # Build GUI components
        self.buildGui()

        # Create observer and attach to parking lot
        self.observer = GUIObserver(self.textField)
        self.parkingLot.attachObserver(self.observer)

    def initVariables(self):
        """
        Initialize all GUI variables as instance variables

        IMPROVEMENT: Encapsulated in class instead of global scope
        """
        # Lot creation variables
        self.numValue = tk.StringVar()
        self.evValue = tk.StringVar()
        self.levelValue = tk.StringVar()
        self.levelValue.set("1")  # Default level

        # Vehicle details variables
        self.makeValue = tk.StringVar()
        self.modelValue = tk.StringVar()
        self.colorValue = tk.StringVar()
        self.regNumValue = tk.StringVar()

        # Boolean variables
        self.isElectric = tk.BooleanVar()
        self.isMotorcycle = tk.BooleanVar()

        # Removal variables
        self.slotValue = tk.StringVar()
        self.removeEv = tk.BooleanVar()

        # Search variables
        self.searchRegNum = tk.StringVar()
        self.searchColor = tk.StringVar()

    def buildGui(self):
        """Build all GUI components"""

        # Header
        tk.Label(
            self.root,
            text='Parking Lot Manager - Refactored',
            font='Arial 14 bold'
        ).grid(row=0, column=0, padx=10, pady=10, columnspan=4)

        # Lot Creation Section
        self.buildLotCreationSection()

        # Vehicle Management Section
        self.buildVehicleSection()

        # Search Section
        self.buildSearchSection()

        # Status Section
        self.buildStatusSection()

        # Output text field
        self.buildOutputSection()

    def buildLotCreationSection(self):
        """Build parking lot creation section"""
        row = 1

        tk.Label(
            self.root,
            text='Lot Creation',
            font='Arial 12 bold'
        ).grid(row=row, column=0, padx=10, columnspan=4)
        row += 1

        # Regular spaces
        tk.Label(
            self.root,
            text='Number of Regular Spaces',
            font='Arial 12'
        ).grid(row=row, column=0, padx=5)

        tk.Entry(
            self.root,
            textvariable=self.numValue,
            width=6,
            font='Arial 12'
        ).grid(row=row, column=1, padx=4, pady=2)

        # EV spaces
        tk.Label(
            self.root,
            text='Number of EV Spaces',
            font='Arial 12'
        ).grid(row=row, column=2, padx=5)

        tk.Entry(
            self.root,
            textvariable=self.evValue,
            width=6,
            font='Arial 12'
        ).grid(row=row, column=3, padx=4, pady=4)
        row += 1

        # Floor level
        tk.Label(
            self.root,
            text='Floor Level',
            font='Arial 12'
        ).grid(row=row, column=0, padx=5)

        tk.Entry(
            self.root,
            textvariable=self.levelValue,
            width=6,
            font='Arial 12'
        ).grid(row=row, column=1, padx=4, pady=4)
        row += 1

        # Create button
        tk.Button(
            self.root,
            text="Create Parking Lot",
            command=self.createLot,
            font="Arial 12",
            bg='lightblue',
            fg='black',
            activebackground="teal",
            padx=5,
            pady=5
        ).grid(row=row, column=0, padx=4, pady=4)

    def buildVehicleSection(self):
        """Build vehicle management section"""
        row = 5

        tk.Label(
            self.root,
            text='Vehicle Management',
            font='Arial 12 bold'
        ).grid(row=row, column=0, padx=10, columnspan=4)
        row += 1

        # Make and Model
        tk.Label(self.root, text='Make', font='Arial 12').grid(row=row, column=0, padx=5)
        tk.Entry(self.root, textvariable=self.makeValue, width=12, font='Arial 12').grid(row=row, column=1, padx=4,
                                                                                          pady=4)

        tk.Label(self.root, text='Model', font='Arial 12').grid(row=row, column=2, padx=5)
        tk.Entry(self.root, textvariable=self.modelValue, width=12, font='Arial 12').grid(row=row, column=3, padx=4,
                                                                                           pady=4)
        row += 1

        # Color and Registration
        tk.Label(self.root, text='Color', font='Arial 12').grid(row=row, column=0, padx=5)
        tk.Entry(self.root, textvariable=self.colorValue, width=12, font='Arial 12').grid(row=row, column=1, padx=4,
                                                                                           pady=4)

        tk.Label(self.root, text='Registration #', font='Arial 12').grid(row=row, column=2, padx=5)
        tk.Entry(self.root, textvariable=self.regNumValue, width=12, font='Arial 12').grid(row=row, column=3, padx=4,
                                                                                         pady=4)
        row += 1

        # Checkboxes - using BooleanVar instead of IntVar
        tk.Checkbutton(
            self.root,
            text='Electric Vehicle',
            variable=self.isElectric,
            font='Arial 12'
        ).grid(column=0, row=row, padx=4, pady=4)

        tk.Checkbutton(
            self.root,
            text='Motorcycle',
            variable=self.isMotorcycle,
            font='Arial 12'
        ).grid(column=1, row=row, padx=4, pady=4)
        row += 1

        # Park button
        tk.Button(
            self.root,
            command=self.parkVehicle,
            text="Park Vehicle",
            font="Arial 11",
            bg='lightblue',
            fg='black',
            activebackground="teal",
            padx=5,
            pady=5
        ).grid(column=0, row=row, padx=4, pady=4)
        row += 1

        # Remove section
        tk.Label(self.root, text='Slot #', font='Arial 12').grid(row=row, column=0, padx=5)
        tk.Entry(self.root, textvariable=self.slotValue, width=12, font='Arial 12').grid(row=row, column=1, padx=4,
                                                                                          pady=4)

        tk.Checkbutton(
            self.root,
            text='EV Slot?',
            variable=self.removeEv,
            font='Arial 12'
        ).grid(column=2, row=row, padx=4, pady=4)
        row += 1

        tk.Button(
            self.root,
            command=self.removeVehicle,
            text="Remove Vehicle",
            font="Arial 11",
            bg='lightblue',
            fg='black',
            activebackground="teal",
            padx=5,
            pady=5
        ).grid(column=0, row=row, padx=4, pady=4)

    def buildSearchSection(self):
        """Build search section"""
        row = 12

        # Search by registration
        tk.Button(
            self.root,
            command=self.searchByRegNum,
            text="Find by Registration #",
            font="Arial 11",
            bg='lightblue',
            fg='black',
            activebackground="teal",
            padx=5,
            pady=5
        ).grid(column=0, row=row, padx=4, pady=4)

        tk.Entry(
            self.root,
            textvariable=self.searchRegNum,
            width=12,
            font='Arial 12'
        ).grid(row=row, column=1, padx=4, pady=4)

        # Search by color
        tk.Button(
            self.root,
            command=self.searchByColor,
            text="Find by Color",
            font="Arial 11",
            bg='lightblue',
            fg='black',
            activebackground="teal",
            padx=5,
            pady=5
        ).grid(column=2, row=row, padx=4, pady=4)

        tk.Entry(
            self.root,
            textvariable=self.searchColor,
            width=12,
            font='Arial 12'
        ).grid(row=row, column=3, padx=4, pady=4)

    def buildStatusSection(self):
        """Build status section"""
        row = 13

        tk.Button(
            self.root,
            command=self.showStatus,
            text="Show All Vehicles",
            font="Arial 11",
            bg='PaleGreen1',
            fg='black',
            activebackground="PaleGreen3",
            padx=5,
            pady=5
        ).grid(column=0, row=row, padx=4, pady=4)

    def buildOutputSection(self):
        """Build output text area"""
        row = 14

        # Create text field as instance variable (Not global)
        self.textField = tk.Text(self.root, width=90, height=15)
        self.textField.grid(column=0, row=row, padx=10, pady=10, columnspan=4)

    # Command Handlers
    def createLot(self):
        """Create parking lot"""
        try:
            capacity = int(self.numValue.get())
            evCapacity = int(self.evValue.get())
            level = int(self.levelValue.get())

            self.parkingLot.createParkingLot(capacity, evCapacity, level)

            message = (
                f'Created parking lot with {capacity} regular slots and '
                f'{evCapacity} EV slots on level: {level}\n'
            )
            self.textField.insert(tk.END, message)

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")

    def parkVehicle(self):
        """Park a vehicle using Factory Pattern"""
        try:
            # Get values from GUI
            regNum = self.regNumValue.get()
            make = self.makeValue.get()
            model = self.modelValue.get()
            color = self.colorValue.get()

            # Determine vehicle type using boolean flags
            isElectric = self.isElectric.get()
            isMotorcycle = self.isMotorcycle.get()

            # Use Factory Pattern to create vehicle
            if isElectric and isMotorcycle:
                vehicleType = VehicleType.ELECTRIC_BIKE
            elif isElectric:
                vehicleType = VehicleType.ELECTRIC_CAR
            elif isMotorcycle:
                vehicleType = VehicleType.MOTORCYCLE
            else:
                vehicleType = VehicleType.CAR

            # Create vehicle using factory
            vehicle = VehicleFactory.createVehicle(
                vehicleType,
                regNum,
                make,
                model,
                color
            )

            # Park the vehicle
            slot = self.parkingLot.park(vehicle, isElectric)

            if slot is None:
                messagebox.showwarning("Full", "Parking lot is full")
            else:
                # Observer automatically displays message
                # Clear form
                self.clearVehicleForm()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def removeVehicle(self):
        """Remove a vehicle from a slot"""
        try:
            slotNumber = int(self.slotValue.get())
            isElectric = self.removeEv.get()  # Boolean, not 0/1

            success = self.parkingLot.leave(slotNumber, isElectric)

            if success:
                # Observer automatically displays message
                self.slotValue.set("")
            else:
                messagebox.showwarning(
                    "Error",
                    f"Unable to remove vehicle from slot {slotNumber}"
                )

        except ValueError:
            messagebox.showerror("Error", "Please enter valid slot number")

    def searchByRegNum(self):
        """Search for vehicle by registration number"""
        regNum = self.searchRegNum.get()

        if not regNum:
            messagebox.showwarning("Warning", "Please enter registration number")
            return

        result = self.parkingLot.findByRegNum(regNum)

        if result:
            slotNumber, isElectric = result
            slotType = "EV" if isElectric else "Regular"
            message = f"Found: {regNum} in {slotType} slot {slotNumber}\n"
            self.textField.insert(tk.END, message)
        else:
            message = f"Vehicle {regNum} not found\n"
            self.textField.insert(tk.END, message)

    def searchByColor(self):
        """Search for vehicles by color"""
        color = self.searchColor.get()

        if not color:
            messagebox.showwarning("Warning", "Please enter color")
            return

        results = self.parkingLot.findByColor(color)

        if results:
            message = f"Found {len(results)} {color} vehicle(s):\n"
            for slotNumber, isElectric in results:
                slotType = "EV" if isElectric else "Regular"
                message += f"  - {slotType} slot {slotNumber}\n"
            self.textField.insert(tk.END, message)
        else:
            message = f"No {color} vehicles found\n"
            self.textField.insert(tk.END, message)

    def showStatus(self):
        """Display current parking lot status: Gets data from parking lot instead of accessing slots directly"""
        status = self.parkingLot.getStatus()

        # Display header
        self.textField.insert(tk.END, "\n" + "=" * 90 + "\n")
        self.textField.insert(tk.END, "PARKING LOT STATUS\n")
        self.textField.insert(tk.END, "=" * 90 + "\n\n")

        # Display regular vehicles
        self.textField.insert(tk.END, "Regular Vehicles:\n")
        self.textField.insert(tk.END, "Slot\tLevel\tReg No.\t\tColor\t\tMake\t\tModel\n")
        self.textField.insert(tk.END, "-" * 90 + "\n")

        if status['regular']:
            for vehicle in status['regular']:
                line = (
                    f"{vehicle['slot']}\t{vehicle['level']}\t"
                    f"{vehicle['registration']}\t\t{vehicle['color']}\t\t"
                    f"{vehicle['make']}\t\t{vehicle['model']}\n"
                )
                self.textField.insert(tk.END, line)
        else:
            self.textField.insert(tk.END, "No vehicles parked\n")

        # Display electric vehicles
        self.textField.insert(tk.END, "\nElectric Vehicles:\n")
        self.textField.insert(tk.END, "Slot\tLevel\tReg No.\t\tColor\t\tMake\t\tModel\t\tCharge\n")
        self.textField.insert(tk.END, "-" * 90 + "\n")

        if status['electric']:
            for vehicle in status['electric']:
                line = (
                    f"{vehicle['slot']}\t{vehicle['level']}\t"
                    f"{vehicle['registration']}\t\t{vehicle['color']}\t\t"
                    f"{vehicle['make']}\t\t{vehicle['model']}\t\t"
                    f"{vehicle['charge']}%\n"
                )
                self.textField.insert(tk.END, line)
        else:
            self.textField.insert(tk.END, "No electric vehicles parked\n")

        self.textField.insert(tk.END, "\n")

    def clearVehicleForm(self):
        """Clear vehicle input form"""
        self.regNumValue.set("")
        self.makeValue.set("")
        self.modelValue.set("")
        self.colorValue.set("")
        self.isElectric.set(False)
        self.isMotorcycle.set(False)
