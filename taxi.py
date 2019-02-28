from Ride import Ride

class Taxi:
    #comment for banter
    
    def __init__(self, id=-1):
        self.ride_number = id
        self.location = [0,0]
        self.ride = None
        self.completedRides = []
        self.riding = False

    def drive(self, step):
        # This function will be responsible for moving a taxi towards
        # either the start or end destination of its current ride,
        # waiting until its current ride is ready
        if self.riding: #If you have picked up passenger
            self.moveTowards(self.ride.finish) #move towards finish
            if self.location == self.ride.finish: #if at destination
                self.rideCompleted() #drop passenger off
        else:
            self.moveTowards(self.ride.start)
            if self.location == self.ride.start:
                self.riding = True
            
        
    def moveTowards(self,destination):
        # changes the location of the taxi to
        # move it towards a given coordinate destination
        if self.location[0] < destination[0]:
            self.location[0] += 1
        elif self.location[0] > destination[0]:
            self.location[0] -= 1
        if self.location[1] < destination[1]:
            self.location[1] += 1
        elif self.location[1] > destination[1]:
            self.location[1] -= 1
            
    def rideCompleted(self):
        self.completedRides.append(self.ride.ride_number)
        self.ride = None
