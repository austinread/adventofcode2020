from helpers import inputs

raw = inputs.import_input(3)
rows = raw.split("\n")

def count_trees(slope_x, slope_y):
    index = 0
    row = 0
    trees = 0

    while(row < len(rows)):
        if rows[row][index] == "#":
            trees += 1
        
        if row >= len(rows)-slope_y:
            break

        row += slope_y
        nextIndex = index + slope_x
        index = nextIndex if nextIndex < len(rows[row]) else nextIndex - len(rows[row])

    return trees

product = count_trees(1,1) * count_trees(3,1) * count_trees(5,1) * count_trees(7,1) * count_trees(1,2)

print(f"Number of Trees A: {count_trees(3,1)}")
print(f"Number of Trees B: {product}")