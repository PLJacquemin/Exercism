# Globals for the directions
# Change the values as you see fit
EAST = [1, 0]
NORTH = [0, 1]
WEST = [-1, 0]
SOUTH = [0, -1]

directions = {
            0: EAST,
            1: NORTH,
            2: WEST,
            3: SOUTH}

class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self.x = x
        self.y = y
        self.coordinates = (self.x, self.y)
        for case, coord in directions.items():
            if coord == direction:
                self.case_dir = case
                self.direction = coord

    def move(self, input=None):
        for command in input:
            if command == "A":
                self.x += self.direction[0]
                self.y += self.direction[1]
                self.coordinates = (self.x, self.y)
            elif command == "R":
                self.case_dir = (self.case_dir-1)%4
                self.direction = directions[self.case_dir]
            elif command == "L":
                self.case_dir = (self.case_dir+1)%4
                self.direction = directions[self.case_dir]
