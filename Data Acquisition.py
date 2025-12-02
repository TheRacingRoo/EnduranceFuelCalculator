from dataclasses import field
from timeit import default_timer
from tkinter.font import names


def driverdata():
    """
    This function takes in driver data for a push stint and a save stint.

    Inputs:
        - Driver Name
        - Driver Lap Time
        - Driver Fuel / Lap

    Output:
        - Consolidated driver data within classes

    """


    class Driver:
        def __init__(self, name, d_time, d_fuel, n_time, n_fuel):
            self.name = name
            self.d_time = d_time
            self.d_fuel = d_fuel
            self.n_time = n_time
            self.n_fuel = n_fuel

    # Driver 1 Data Acquisition

    name1 = "Joey"      #Driver Name
    d_time1 = 120       #Daytime Laptimes [Fuel Save , Full Push]
    d_fuel1 = 0.87
    n_time1 = 118
    n_fuel1 = 0.86


    d1_dat = Driver(name1, d_time1, d_fuel1, n_time1, n_fuel1)

