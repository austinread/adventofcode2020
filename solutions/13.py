from helpers import inputs

raw = inputs.import_input(13)
lines = raw.split("\n")

earliest_depart_time = int(lines[0])

bus_schedule = lines[1]
buses = bus_schedule.split(",")

def get_best_departure_time():
    best_time = None
    for b in buses:
        if b == "x":
            continue    #out of service

        b = int(b)
        i = 0
        while True:
            departure_time = b * i
            if departure_time > earliest_depart_time:
                if best_time == None or departure_time < best_time:
                    best_time = departure_time
                    best_bus = b
                break
            i += 1

    print(f"The best bus to get on is ID# {best_bus}, which requires waiting {best_time - earliest_depart_time} minutes.  Answer: {best_bus * (best_time - earliest_depart_time)}")
    
get_best_departure_time()