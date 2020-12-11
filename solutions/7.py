from helpers import inputs

raw = inputs.import_input(7)
bags_raw = raw.split("\n")

class Bag:
    def __init__(self, color):
        self.color = color
        self.subbags = {}

    def add_subbag(self, number, color):
        self.subbags[color] = number

    def count_total_subbags(self, all_bags):
        total = 0
        if len(self.subbags) > 0:

            for color in self.subbags:
                total += int(self.subbags[color])

            for color in self.subbags:
                subbag = get_bag_by_color(color, all_bags)
                total += subbag.count_total_subbags(all_bags) * int(self.subbags[color])

        return total


def get_bag_by_color(color, bags):
    for bag in bags:
        if bag.color == color:
            return bag
        
    return None

def does_bag_contain_color(color, bag, bags):
    if len(bag.subbags) == 0:
        return False
    elif color in bag.subbags:
        return True
    else:
        for subbag_color in bag.subbags:
            subbag = get_bag_by_color(subbag_color, bags)
            if does_bag_contain_color(color, subbag, bags):
                return True
        return False

bags = []
for raw in bags_raw:
    bag = Bag(raw[0: raw.index(" bags")])

    contain_str = raw.split("contain ",1)[1]

    if contain_str == "no other bags.":
        bags.append(bag)
        continue
    else:
        subbags = contain_str.split(", ")
        for subbag in subbags:
            #none of the numbers are more than 1 digit, conveniently
            bag.add_subbag(subbag[0], subbag[2:subbag.index(" bag")])

    bags.append(bag)

target_bags = []
for bag in bags:
    if does_bag_contain_color("shiny gold", bag, bags):
        target_bags.append(bag)

shiny_gold_bag = get_bag_by_color("shiny gold", bags)

print(f"Number of bags that can hold shiny gold bags: {len(target_bags)}")
print(f"Shiny Gold bags contain: {shiny_gold_bag.count_total_subbags(bags)} bags")