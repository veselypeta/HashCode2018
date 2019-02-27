from Ride import Ride

class Taxi:
    location = (0,0)
    ride = None
    completedRides = []
    
    def drive(self):
        # This function will be responsible for moving a taxi towards
        # either the start or end destination of its current ride,
        # waiting until its current ride is ready,
        # or nothing if it doesnt have a ride
        self.rideCompleted()
        
    def move(destination):
        # this function will changed the location of the taxi to
        # move it towards a given coordinate destination
        pass

    def rideCompleted(self):
        self.completedRides.append(self.ride.ride_number)
        self.ride = None
        
