from helpers import inputs, boats

raw = inputs.import_input(12)
instructions = raw.split("\n")

HMSMonty = boats.Boat_v1()
for i in instructions:
    HMSMonty.execute(i)

HMSSpam = boats.Boat_v2()
for i in instructions:
    HMSSpam.execute(i)

print(f"Manhattan Distance of the Good Ship HMS Monty: {HMSMonty.manhattan_distance}")
print(f"Manhattan Distance of the Good Ship HMS Spam: {HMSSpam.manhattan_distance}")