from Ride import Ride
from City import City
from taxi import Taxi

def parse_data(filename):
    with open(filename, 'r') as data_file:
        lines = [x.strip('\n') for x in data_file.readlines()]
        n_rows, n_columns, n_vehicles, n_rides, ride_bonus, n_steps = map(int, tuple(lines[0].split(' ')))
        theCity = City(n_rows, n_columns, n_vehicles, n_rides, ride_bonus, n_steps)
        ridesList = [list(map(int, x)) for x in [y.split(" ") for y in lines[1:]]]
        rideObjects = [Ride(*tuple(x)) for x in ridesList]
        return theCity, rideObjects

city, rides = parse_data("b_should_be_easy.in")
for r in rides:
        print(r)



# create ride queues and taxi queue
# then figure out how to sort the queue
def simulation(city, rides):
    for ride in rides:
        print(ride.ride_number)
    taxis = [Taxi() for i in range(city.n_rides)]
    
    for step in range(city.n_steps):
        for taxi in taxis:
            if taxi.ride == None:
                if rides:
                    taxi.ride = rides.pop() #assign it a ride
            else:
                taxi.drive() #do something with ride
                
    for taxi in taxis:
        print(taxi.completedRides)
        
    
# city, rides = parse_data("a_example.in")
# simulation(city, rides) 
