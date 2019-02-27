from Ride import Ride
from City import City
from taxi import Taxi

def parse_data(filename):
    with open(filename, 'r') as data_file:
        lines = [x.strip('\n') for x in data_file.readlines()]
        n_rows, n_columns, n_vehicles, n_rides, ride_bonus, n_steps = map(int, tuple(lines[0].split(' ')))
        theCity = City(n_rows, n_columns, n_vehicles, n_rides, ride_bonus, n_steps)
        ridesList = [list(map(int, x)) for x in [y.split(" ") for y in lines[1:]]]
        ridesNumber = [list(x + [i]) for i,x in enumerate(ridesList)]
        rideObjects = [Ride(*tuple(x)) for x in ridesNumber]
        return theCity, rideObjects

city, rides = parse_data("a_example.in")
for r in rides:
        print(r)


# create ride queues and taxi queue
# then figure out how to sort the queue
def simulation(city, rides):
    taxis = [Taxi() for i in range(city.n_rides)]
    
    for step in range(city.n_steps):
        for taxi in taxis:
            if taxi.ride == None and rides: #If taxi does not have a ride and there are rides left
                taxi.ride = rides.pop() #Just assign it the first taxi in the queue
            else:
                taxi.drive() # do something with the ride

    #print which taxi completed which ride         
    for taxi in taxis:
        print(taxi.completedRides)
        
    
city, rides = parse_data("a_example.in")
simulation(city, rides) 
