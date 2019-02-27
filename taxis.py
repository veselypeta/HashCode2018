from Ride import Ride
from City import City

def parse_data(filename):
    with open(filename, 'r') as data_file:
        lines = [x.strip('\n') for x in data_file.readlines()]
        n_rows, n_columns, n_vehicles, n_rides, ride_bonus, n_steps = map(int, tuple(lines[0].split(' ')))
        theCity = City(n_rows, n_columns, n_vehicles, n_rides, ride_bonus, n_steps)
        ridesList = [x for x in map(lines[1:]]

        return theCity, rides

city, rides = parse_data("b_should_be_easy.in")