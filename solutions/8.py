import sys
from helpers import inputs

raw = inputs.import_input(8)
instructions = raw.split("\n")

class Gameboy:
    def __init__(self, instructions):
        self.accumulator = 0
        self.instructions = instructions
        self.executed_instructions = []

    def execute_line(self, line):
        if line == len(self.instructions):
            print(f"program terminated, current accumulator value: {self.accumulator}")
            sys.exit()

        if line < 0 or line > len(self.instructions):
            print(f"error attempting to run non-existent line {line+1}")
            return

        if not self.executed_instructions.__contains__(line):
            self.executed_instructions.append(line)
            instruction = self.instructions[line]
            operation = instruction[0:3]
            argument = int(instruction[4:])

            if operation == "acc":
                self.accumulator += argument
                self.execute_line(line+1)
            elif operation == "jmp":
                self.execute_line(line + argument)
            elif operation == "nop":
                self.execute_line(line+1)

        else:
            print(f"infinite loop detected, current accumulator value: {self.accumulator}")

    def start(self):
        self.execute_line(0)

gb = Gameboy(instructions)
gb.start()

#brute-force figure out which instruction change results in a terminating program
jmps = []
nops = []
for i in range(len(instructions)):
    if instructions[i][0:3] == "jmp":
        jmps.append(i)
    elif instructions[i][0:3] == "nop":
        nops.append(i)

for j in jmps:
    print(f"changing line {j+1} from jmp to nop")
    original_instruction = instructions[j]
    tweaked_instructions = instructions.copy()
    tweaked_instructions[j] = f"nop{original_instruction[4:]}"

    Gameboy(tweaked_instructions).start()

for n in nops:
    print(f"changing line {n+1} from nop to jmp")
    original_instruction = instructions[n]
    tweaked_instructions = instructions.copy()
    tweaked_instructions[n] = f"jmp{original_instruction[4:]}"

    Gameboy(tweaked_instructions).start()