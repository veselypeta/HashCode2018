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

#for r in rides:
#   print(r)


# create ride queues and taxi queue
# then figure out how to sort the queue
def simulation(city, rides):
    taxis = [Taxi(i) for i in range(city.n_vehicles)]
    
    for step in range(city.n_steps):
        for taxi in taxis:
            if taxi.ride == None:
                if rides: #If taxi does not have a ride and there are rides left
                    taxi.ride = rides.pop(0) #Just assign it the first taxi in the queue
                    taxi.drive(step)
            else:
                taxi.drive(step) # do something with the ride

    #print which taxi completed which ride         
    for taxi in taxis:
        print(taxi.completedRides)
        
    
city, rides = parse_data("b_should_be_easy.in")
simulation(city, rides) 
