import inputs

raw = inputs.import_input(2)
passwords_raw = raw.split("\n")

class Password:
    def __init__(self, raw):
        self.password = raw[raw.index(": ")+2:]
        self.key = raw[raw.index(":")-1]
        self.key_a = int(raw[0:raw.index("-")])
        self.key_b = int(raw[raw.index("-")+1:raw.index(" ")])


passwords = [Password(p) for p in passwords_raw]

#key_a and key_b are the mininum and maxiumum appearances of the key
def validate_v1():
    correct_password_count = 0
    for p in passwords:
        key_count = p.password.count(p.key)
        if key_count >= p.key_a and key_count <= p.key_b:
            correct_password_count += 1

    return correct_password_count


#the key must be present in the index represented by key_a OR key_b, but not both
def validate_v2():
    correct_password_count = 0
    for p in passwords:
        if(p.password[p.key_a-1] == p.key and p.password[p.key_b-1] != p.key) or (p.password[p.key_b-1] == p.key and p.password[p.key_a-1] != p.key):
            correct_password_count += 1

    return correct_password_count

print (f"Solution 2A: {str(validate_v1())}")
print (f"Solution 2B: {str (validate_v2())}")