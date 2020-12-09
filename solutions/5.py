import sys
from helpers import inputs

raw = inputs.import_input(5)
passes_raw = raw.split("\n")

def binary_space_partition(code, lower_signifier, upper_signifier):
    range_min = 0
    range_max = pow(2, len(code))-1

    for i in range(len(code)):
        if code[i] == lower_signifier:
            range_max -= (range_max-range_min+1)/2
        elif code[i] == upper_signifier:
            range_min += (range_max-range_min+1)/2
        else:
            print(f"invalid code at position: {i}")
            sys.exit()

    if range_min != range_max:
        print(f"range_min does not equal range_max: {range_min}, {range_max}")
        sys.exit()

    return int(range_min)

def get_id_by_pass(boarding_pass):
    row_code = boarding_pass[0:7]
    column_code = boarding_pass[7:]

    row = binary_space_partition(row_code, "F", "B")
    column = binary_space_partition(column_code, "L", "R")

    return row * 8 + column

ids = sorted([get_id_by_pass(p) for p in passes_raw])

missing_id = -1
for i in range(len(ids)-2):
    if ids[i+1] == ids[i]+2:
        missing_id = ids[i]+1
        break

if missing_id == -1:
    print("no missing id found")
    sys.exit()


print(f"Highest Seat ID: {max(ids)}")
print(f"My Seat ID: {missing_id}")