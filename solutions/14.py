from helpers import inputs, dynamic_list

raw = inputs.import_input(14)
lines = raw.split("\n")

memoryA = dynamic_list.DynamicBinaryListV1("000000000000000000000000000000000000", "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
memoryB = dynamic_list.DynamicBinaryListV2(0, "000000000000000000000000000000000000")

def parse_mask(txt):
    return txt[txt.index("= ")+2:]

def parse_action(txt):
    address = int(txt[txt.index("[")+1:txt.index("]")])
    value = int(txt[txt.index("= ")+2:])
    return (address,value)

for line in lines:
    if line[0:4] == "mask":
        memoryA.mask = parse_mask(line)
    elif line[0:3] == "mem":
        action = parse_action(line)
        memoryA.set_value(action[0], action[1])

for line in lines:
    if line[0:4] == "mask":
        memoryB.mask = parse_mask(line)
    elif line[0:3] == "mem":
        action = parse_action(line)
        memoryB.set_value(action[0], action[1])

print(f"Sum of all non-zero values: {memoryA.sum_values()}")
print(f"Sum of all non-zero values: {memoryB.sum_values()}")