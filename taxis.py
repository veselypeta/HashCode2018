from Ride import Ride
from City import City
from taxi import Taxi

# parse the data from the file
def parse_data(filename):
    with open(filename, 'r') as data_file:
        # readlines
        lines = [x.strip('\n') for x in data_file.readlines()]
        # process the first line
        n_rows, n_columns, n_vehicles, n_rides, ride_bonus, n_steps = map(int, tuple(lines[0].split(' ')))
        # create a city class to hold this data
        theCity = City(n_rows, n_columns, n_vehicles, n_rides, ride_bonus, n_steps)
        # The remaining lines are rides - which are processed and added to a list of ride objects
        ridesList = [list(map(int, x)) for x in [y.split(" ") for y in lines[1:]]]
        ridesNumber = [list(x + [i]) for i,x in enumerate(ridesList)]
        rideObjects = [Ride(*tuple(x)) for x in ridesNumber]
        return theCity, rideObjects

city, rides = parse_data("b_should_be_easy.in")
taxis = [Taxi(id=i) for i in range(city.n_rides)]



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
