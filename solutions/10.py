from helpers import inputs

raw = inputs.import_input(10)
adapters = raw.split("\n")
adapters = [int(a) for a in adapters]

outlet_j = 0
device_j = max(adapters)+3
adapter_chain = []
joltage_tolerance = 3

#get ordered list of adapters to connect together
previous_j = outlet_j
while len(adapters) > 0:
    possible_links = []
    for a in adapters:
        if a > previous_j and a-previous_j <= joltage_tolerance:
            possible_links.append(a)
    
    previous_j = min(possible_links)
    adapter_chain.append(previous_j)
    adapters.remove(previous_j)

#get list of joltage differences
differences = []
for a in range(0,len(adapter_chain)):
    if a == 0:
        differences.append(adapter_chain[a]-outlet_j)
    else:
        differences.append(adapter_chain[a]-adapter_chain[a-1])
differences.append(device_j-adapter_chain[len(adapter_chain)-1])

#count the difference and get part 1 answer
one_j_differences = differences.count(1)
three_j_differences = differences.count(3)
print(f"1j differences multiplied by 3j differences: {one_j_differences * three_j_differences}")