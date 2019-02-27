class Ride:
    start = (-1,-1)
    end = (-1,-1)
    earliest = -1
    latest = -1

    def __init__(self,start,end,earliest,latest):
        self.start = start
        self.end = end
        self.earliest = earliest
        self.latest = latest

