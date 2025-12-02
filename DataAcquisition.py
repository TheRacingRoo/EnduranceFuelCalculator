from lib2to3.pgen2.driver import Driver
from pickletools import string1


def stint_length(driver_data,num_driver, car):

    class Stint:
        def __init__(self,name):#,d_laps,d_length,n_laps,n_length):
            self.name = name
            #self.d_laps = d_laps
            #self.d_length = d_length
            #self.n_laps = n_laps
            #self.n_length = n_length

    #Initialize Stint Names in object for loop
    s1 = Stint(driver_data[0].name)
    s2 = Stint(driver_data[1].name)
    s3 = Stint(driver_data[2].name)
    s4 = Stint(driver_data[3].name)

    stint = [s1,s2,s3,s4]

    for i in range(0,num_driver-1):
        data_i = driver_data[i]

        stint[i].d_s_laps = car.fuel_cap / data_i.d_fuel[0] * 1.0    #Calculate day laps, store in stint class, from driver data class (SAVE)

        stint[i].d_p_laps = car.fuel_cap / data_i.d_fuel[1] * 1.0  #Calculate day laps, store in stint class, from driver data class (PUSH)

        stint[i].n_s_laps = car.fuel_cap / data_i.n_fuel[0] * 1.0    #Calculate night laps, store in stint class, from driver data class (SAVE)

        stint[i].n_p_laps = car.fuel_cap / data_i.n_fuel[1] * 1.0  # Calculate night laps, store in stint class, from driver data class (SAVE)

        stint[i].d_s_length = round((data_i.d_time[0] * stint[i].d_s_laps)/60.0,3)   #Calculate day stint length, store in stint class, from driver data class

        stint[i].d_p_length = round((data_i.d_time[1] * stint[i].d_p_laps)/60.0,3) # Calculate day stint length, store in stint class, from driver data class

        stint[i].n_s_length = round((data_i.n_time[0] * stint[i].n_s_laps)/60.0,3)  ##Calculate night stint length, store in stint class, from driver data class

        stint[i].n_p_length = round((data_i.n_time[1] * stint[i].n_p_laps)/60.0,3) ##Calculate night stint length, store in stint class, from driver data class

    print(stint[1].d_p_length)
    print(stint[1].d_p_laps)

    return



def main():

    class Driver:
        def __init__(self, name, d_time, d_fuel, n_time, n_fuel):
            self.name = name
            self.d_time = d_time
            self.d_fuel = d_fuel
            self.n_time = n_time
            self.n_fuel = n_fuel

    num_driver = 4

    # Driver 1 Data Acquisition

    name1 = "Joey"      #Driver Name
    d_time1 = [120,118]       #Day Lap Times [Fuel Save , Full Push] in seconds
    d_fuel1 = [0.80,0.87]     #Day Fuel Usage / Lap [Fuel Save , Full Push] in gallons / lap
    n_time1 = [118,117.2]     #Night Lap Times [Fuel Save , Full Push]
    n_fuel1 = [0.79,0.86]     #Night Fuel Usage / Lap [Fuel Save , Full Push] in gallons / lap

    # Driver 2 Data Acquisition

    name2 = "Mike"  # Driver Name
    d_time2 = [121.5, 119.5]  # Day Lap Times [Fuel Save , Full Push] in seconds
    d_fuel2 = [0.82, 0.89]  # Day Fuel Usage / Lap [Fuel Save , Full Push] in gallons / lap
    n_time2 = [119.5, 118.7]  # Night Lap Times [Fuel Save , Full Push]
    n_fuel2 = [0.81, 0.87]  # Night Fuel Usage / Lap [Fuel Save , Full Push] in gallons / lap

    # Driver 3 Data Acquisition

    name3 = "Nick"  # Driver Name
    d_time3 = [120, 118.2]  # Day Lap Times [Fuel Save , Full Push] in seconds
    d_fuel3 = [0.82, 0.89]  # Day Fuel Usage / Lap [Fuel Save , Full Push] in gallons / lap
    n_time3 = [118.2, 117.5]  # Night Lap Times [Fuel Save , Full Push]
    n_fuel3 = [0.81, 0.87]  # Night Fuel Usage / Lap [Fuel Save , Full Push] in gallons / lap

    # Driver 4 Data Acquisition

    name4 = "Jack"  # Driver Name
    d_time4 = [121, 118.7]  # Day Lap Times [Fuel Save , Full Push] in seconds
    d_fuel4 = [0.83, 0.89]  # Day Fuel Usage / Lap [Fuel Save , Full Push] in gallons / lap
    n_time4 = [118.7, 118]  # Night Lap Times [Fuel Save , Full Push]
    n_fuel4 = [0.83, 0.87]  # Night Fuel Usage / Lap [Fuel Save , Full Push] in gallons / lap

    #If another driver data set is required, change number of drivers and add another driver acquisition here
    #This section will be for driver 5


    #Assign Driver data to Driver Class
    d1_dat = Driver(name1, d_time1, d_fuel1, n_time1, n_fuel1)
    d2_dat = Driver(name2, d_time2, d_fuel2, n_time2, n_fuel2)
    d3_dat = Driver(name3, d_time3, d_fuel3, n_time3, n_fuel3)
    d4_dat = Driver(name4, d_time4, d_fuel4, n_time4, n_fuel4)

    driver_data = [d1_dat,d2_dat,d3_dat,d4_dat]         #Package data to send to function


    #Define race parameters including start time, length, and sunset/sunrise hours
    class Race:
        def __init__(self,length, ig_start, irl_start, sunset, sunrise, warmup_length, quali_length, special):
            self.length = length
            self.ig_start = ig_start
            self.irl_start = irl_start
            self.sunset = sunset
            self.sunrise = sunrise
            self.warmup_length = warmup_length
            self.quali_length = quali_length
            self.special =special

    race_length = 24                             #Race length in hours
    in_game_start = 720   #Note:Noon         #In game start time of warmup session (Minutes after Midnight)
    irl_start =  960    #Note:4pm           #IRL start time of the race server (when you enter warmup)
    in_game_sunset = 1140 #Note:7pm           #In game sunset time (Minutes from midnight)
    in_game_sunrise = 360 #Note:6am          #In game sunrise time (Minutes from midnight)
    warmup_length = 30                     #Length of special event warmup in minutes
    quali_length = 8                       #Quali length for event
    special_event = 1                     #1 for yes(warmup will be applied), 2 for no

    r_prop = Race(race_length,in_game_start,irl_start,in_game_sunset,in_game_sunrise,warmup_length,quali_length,special_event)


    #Define Car Class containing vehicle limitations
    class Car:
        def __init__(self, name, fuel_cap):
            self.name = name
            self.fuel_cap = fuel_cap

    car_name = "Cadillac V-Series GTP"   #Vehicle Name for Reference
    fuel_capacity = 20              #Maximum fuel capacity in gallons (units shouldn't matter though)

    car = Car(car_name, fuel_capacity)


    stint_length(driver_data,num_driver, car)


















if __name__ == "__main__":
    main()