# Globals for the directions
# Change the values as you see fit
EAST = (1, 0, 0, 2)
NORTH = (0, 1, 3, 1)
WEST = (-1, 0, 2, 0)
SOUTH = (0, -1, 1, 3)
COMPASS = [NORTH, EAST, SOUTH, WEST]


class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self.direction = direction
        self.coordinates = (x, y)

    def move(self, command):
        locate = [self.coordinates[0], self.coordinates[1]]
        turn = None
        for com in command:
            if com.upper() == "A":
                locate[0] += self.direction[0]
                locate[1] += self.direction[1]
            if com.upper() == "L":
                self.direction = COMPASS[self.direction[2]]
            elif com.upper() == "R":
                self.direction = COMPASS[self.direction[3]]
        self.coordinates = (locate[0], locate[1])
