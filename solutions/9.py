import sys
from helpers import inputs

raw = inputs.import_input(9)
numbers = raw.split("\n")
numbers = [int(n) for n in numbers]

preamble_length = 25

def is_valid(index):
    number = numbers[index]
    options = numbers[index-preamble_length:index]
    valid = False
    for o1 in options:
        if valid:
            break

        for o2 in options:
            if o1 == o2:
                continue
            if o1 + o2 == number:
                valid = True
                break

    return valid

invalid_number = -1
for n in range (preamble_length,len(numbers)):
    if not is_valid(n):
        invalid_number = numbers[n]
        print(f"Invalid number detected: {invalid_number}")
        break

if invalid_number == -1:
    print("Error: invalid number not found")
    sys.exit()

for i in range(len(numbers)):
    n = numbers[i]
    if n >= invalid_number:
        print("Error: no contiguous sequence found")
        sys.exit()

    sequence = [n]
    for p in range(i+1,len(numbers)):
        n2 = numbers[p]
        sequence.append(n2)

        sequence_sum = sum(sequence)
        if sequence_sum == invalid_number:
            lower = min(sequence)
            upper = max(sequence)

            print(f"Encryption weakness found: {lower + upper}")
            sys.exit()
        if sequence_sum > invalid_number:
            break