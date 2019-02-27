from Ride import Ride

class Taxi:
    
    
    def __init__(self, id=-1):
        self.taxi_number = id
        self.current_location = (0,0)
        self.ride = None
        self.completedRides = []

    def drive(self):
        # This function will be responsible for moving a taxi towards
        # either the start or end destination of its current ride,
        # waiting until its current ride is ready,
        # or nothing if it doesnt have a ride
        self.rideCompleted()
        
    def move(self,destination):
        # this function will changed the location of the taxi to
        # move it towards a given coordinate destination
        pass

    def rideCompleted(self):
        self.completedRides.append(self.ride.ride_number)
        self.ride = None
    
    def get_distance(self, a, b):
        x1, y1 = a
        x2, y2 = b
        return abs(x1 - x2) + abs(y1-y2)

    def calculate_cost(self, nextRide):
        # cost or remaining ride
        if self.ride is not None:
            ride_cost = self.get_distance(self.ride.finish, self.current_location)
            next_ride_cost = self.get_distance(self.ride.finish,  nextRide.start)
        else:
            ride_cost = 0
            next_ride_cost = self.get_distance(self.current_location, nextRide.start)
        
        next_ride_distance = nextRide.distance_to_destination()

        return ride_cost + next_ride_cost + next_ride_distance

        
        


        
