from Ride import Ride
from City import City

def parse_data(filename):
    with open(filename, 'r') as data_file:
        lines = [x.strip('\n') for x in data_file.readlines()]
        n_rows, n_columns, n_vehicles, n_rides, ride_bonus, n_steps = map(int, tuple(lines[0].split(' ')))
        theCity = City(n_rows, n_columns, n_vehicles, n_rides, ride_bonus, n_steps)
        ridesList = [list(map(int, x)) for x in [y.split(" ") for y in lines[1:]]]
        rideObjects = [Ride(*tuple(x)) for x in ridesList]
        return theCity, rideObjects

city, rides = parse_data("b_should_be_easy.in")