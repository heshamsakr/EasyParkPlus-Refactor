from parking_manager import ParkingManager
import tkinter as tk

# Main Entry Point
def main():
    """Application entry point: Creates single instance, no globals"""
    root = tk.Tk()
    app = ParkingManager.ParkingManagerGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()