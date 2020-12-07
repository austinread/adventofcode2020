import inputs

raw = inputs.import_input(1)

entries = raw.split("\n")
entries = [int(e) for e in entries]

def match_two():
    for i1 in range(0, len(entries)-1):
        for i2 in range(i1+1, len(entries)-1):
            if entries[i1] + entries[i2] == 2020:
                return(entries[i1]*entries[i2])


def match_three():
    for i1 in range(0, len(entries)-1):
        for i2 in range(i1+1, len(entries)-1):
            for i3 in range(i2+1, len(entries)-1):
                if entries[i1] + entries[i2] + entries[i3] == 2020:
                    return(entries[i1]*entries[i2]*entries[i3])


print (f"Solution 1A: {str(match_two())}")
print (f"Solution 1B: {str(match_three())}")