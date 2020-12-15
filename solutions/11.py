import sys
from helpers import inputs

raw = inputs.import_input(11)
positions = raw.split("\n")
positions = [list(r) for r in positions]

#debug
def print_seat_map():
    s = ""
    for row in positions:
        for seat in row:
          s += seat
        s += "\n"

    print(s + "\n\n")

def count_filled_seats():
    count = 0
    for row in positions:
        count += row.count("#")

    return count

def get_nearby_seats_v1(r,s):
    row = positions[r]
    nearby_seats = []
    if s < len(row)-1:
        nearby_seats.append(positions[r][s+1])
    if s > 0:
        nearby_seats.append(positions[r][s-1])

    if r > 0:
        nearby_seats.append(positions[r-1][s])
        if s < len(row)-1:
            nearby_seats.append(positions[r-1][s+1])
        if s > 0:
            nearby_seats.append(positions[r-1][s-1])

    if r < len(positions)-1:
        nearby_seats.append(positions[r+1][s])
        if s < len(row)-1:
            nearby_seats.append(positions[r+1][s+1])
        if s > 0:
            nearby_seats.append(positions[r+1][s-1])

    return nearby_seats

def get_nearby_seats_v2(r,s):
    row = positions[r]
    nearby_seats = []

    def get_visible_seat(r1,s1):
        #seperate loop in order to save the original values of x and y
        def recursive_seat_search(r2,s2):
            seat = positions[r+r2][s+s2]
            if seat == ".":
                next_r = r+r1+r2
                next_s = s+s1+s2
                if next_r >= 0 and next_r < len(positions) and next_s >= 0 and next_s < len(row):
                    return recursive_seat_search(r1+r2,s1+s2)
                else:
                    return seat
            else:
                return seat
        return recursive_seat_search(r1,s1)

    if s < len(row)-1:
        nearby_seats.append(get_visible_seat(0,1))
    if s > 0:
        nearby_seats.append(get_visible_seat(0,-1))

    if r > 0:
        nearby_seats.append(get_visible_seat(-1,0))
        if s < len(row)-1:
            nearby_seats.append(get_visible_seat(-1,1))
        if s > 0:
            nearby_seats.append(get_visible_seat(-1,-1))

    if r < len(positions)-1:
        nearby_seats.append(get_visible_seat(1,0))
        if s < len(row)-1:
            nearby_seats.append(get_visible_seat(1,1))
        if s > 0:
            nearby_seats.append(get_visible_seat(1,-1))

    return nearby_seats

def import_humans(question_part):
    seats_filled = []
    seats_emptied = []

    for r in range(0,len(positions)):
        row = positions[r]
        for s in range(0,len(row)):
            seat = positions[r][s]
            #get a list of nearby seats (different depending on part 1 or 2 rules)
            if question_part == 1:
                nearby_seats = get_nearby_seats_v1(r,s)
            elif question_part == 2:
                nearby_seats = get_nearby_seats_v2(r,s)
            else:
                print(f"Developer error, invalid question_part")
                sys.exit()

            #rule 1: fill if there are no occupied nearby seats
            if seat == "L" and not nearby_seats.__contains__("#"):
                seats_filled.append((r,s))

            #rule 2: empty if there are four/five or more occupied seats, differing depending on question part
            if question_part == 1:
                crowd_tolerance = 4
            elif question_part == 2:
                crowd_tolerance = 5

            if seat == "#" and nearby_seats.count("#") >= crowd_tolerance:
                seats_emptied.append((r,s))

    #Keep going until equilibrium is reached
    if len(seats_filled) + len(seats_emptied) == 0:
        #print_seat_map()
        print(f"Seating has stabilized, filled seats: {count_filled_seats()}")
    else:
        for x in seats_filled:
            row = positions[x[0]]
            row[x[1]] = "#"
        for x in seats_emptied:
            row = positions[x[0]]
            row[x[1]] = "L"
        #print_seat_map()
        import_humans(question_part)

import_humans(1)
#reset in between runs
positions = raw.split("\n")
positions = [list(r) for r in positions]
import_humans(2)