class Ride:


    def __init__(self,start_row = -1, start_column = -1,end_row=-1, end_column = -1, earliest=-1,latest=-1):
        self.start = (start_row, start_column)
        self.finish = (end_row, end_column)
        self.earliest = earliest
        self.latest = latest


    def calculate_distance(self):
        return abs(self.finish[0] - self.start[0]) + abs(self.finish[1]- self.start[1])

