import re

class Boat_v1:
    def __init__(self):
        self.origin = (0,0)
        self.x = self.origin[0]
        self.y = self.origin[1]
        self.dir = 0    #0/359 where 0 = East

    @property
    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)

    def __rotate(self, degrees):
        self.dir += degrees
        if self.dir < 0:
            self.dir = 360+self.dir
        elif self.dir > 359:
            self.dir = self.dir-360

    def execute(self, instruction):
        action = instruction[0]
        value = int(instruction[1:])

        if action == "R":
            self.__rotate(value)
        elif action == "L":
            self.__rotate(-value)
        elif action == "N":
            self.y += value
        elif action == "S":
            self.y -= value
        elif action == "E":
            self.x += value
        elif action == "W":
            self.x -= value
        elif action == "F":
            #Rotations are conveniently only given in 90 degree intervals
            if self.dir == 0:   #E
                self.x += value
            elif self.dir == 180:   #W
                self.x -= value
            elif self.dir == 270:   #N
                self.y += value
            elif self.dir == 90:   #S
                self.y -= value


class Boat_v2:
    def __init__(self):
        self.origin = (0,0)
        self.waypoint_origin = (10,1)

        #these values are relative to the position of the ship, not absolute
        self.waypoint_x = self.waypoint_origin[0]
        self.waypoint_y = self.waypoint_origin[1]

        self.x = self.origin[0]
        self.y = self.origin[1]

    @property
    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)

    def __rotate_waypoint(self, degrees, direction):
        #Rotations are conveniently only given in 90 degree intervals
        if direction == "R":
            multiplier = -1
        elif direction == "L":
            multiplier = 1

        if abs(degrees) == 90:
            new_x = -self.waypoint_y * multiplier
            new_y = self.waypoint_x * multiplier
            self.waypoint_x = new_x
            self.waypoint_y = new_y
        if abs(degrees) == 180:
            new_x = -self.waypoint_x
            new_y = -self.waypoint_y
            self.waypoint_x = new_x
            self.waypoint_y = new_y
        if abs(degrees) == 270:
            new_x = self.waypoint_y * multiplier
            new_y = -self.waypoint_x * multiplier
            self.waypoint_x = new_x
            self.waypoint_y = new_y

    def execute(self, instruction):
        action = instruction[0]
        value = int(instruction[1:])

        if action == "R" or action == "L":
            self.__rotate_waypoint(value, action)
        elif action == "N":
            self.waypoint_y += value
        elif action == "S":
            self.waypoint_y -= value
        elif action == "E":
            self.waypoint_x += value
        elif action == "W":
            self.waypoint_x -= value
        elif action == "F":
            self.x += value * self.waypoint_x
            self.y += value * self.waypoint_y