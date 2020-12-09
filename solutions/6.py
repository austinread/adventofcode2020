from helpers import inputs

raw = inputs.import_input(6)
groups_raw = raw.split("\n\n")

def sum_unique_answers():
    group_totals = []

    for group in groups_raw:
        answer_sheets = group.split("\n")

        affirmative_answers = []
        for sheet in answer_sheets:
            for i in range(len(sheet)):
                if not affirmative_answers.__contains__(sheet[i]):
                    affirmative_answers.append(sheet[i])

        group_totals.append(len(affirmative_answers))
    
    return sum(group_totals)

def sum_consistent_answers():
    group_totals = []

    for group in groups_raw:
        answer_sheets = group.split("\n")

        affirmative_answers = []

        #after writing this extremely manual method, I learned about set(a).intersection(b), which could be utilized in a looping fashion
        for sheet in answer_sheets:
            for i in range(len(sheet)):
                #do all other sheets contain this answer?
                if not affirmative_answers.__contains__(sheet[i]):
                    all_group_members_affirmative = True
                    for s in answer_sheets:
                        if not s.__contains__(sheet[i]):
                            all_group_members_affirmative = False
                            break
                    if all_group_members_affirmative:
                        affirmative_answers.append(sheet[i])

        group_totals.append(len(affirmative_answers))
    
    return sum(group_totals)

print(f"Sum of All Group Yes Answers: {sum_unique_answers()}")
print(f"Sum of All Consistent Group Yes Answers: {sum_consistent_answers()}")