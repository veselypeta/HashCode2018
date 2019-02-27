class Ride:


    def __init__(self,start_row = -1, start_column = -1,end_row=-1, end_column = -1, earliest=-1,latest=-1, id = -1):
        self.start = (start_row, start_column)
        self.finish = (end_row, end_column)
        self.earliest = earliest
        self.latest = latest
        self.ride_number = id
    
    def __str__(self):
        return "Ride number {} from start {} to finish {}, earliest time {} , latest time {}".format(
            self.ride_number, self.start, self.finish, self.earliest, self.latest)


    def distance_to_destination(self):
        return abs(self.finish[0] - self.start[0]) + abs(self.finish[1]- self.start[1])

