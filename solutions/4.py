from helpers import inputs, passport

raw = inputs.import_input(4)
passports_raw = raw.split("\n\n")

passports = [passport.Passport(p) for p in passports_raw]

passports_with_all_fields = 0
for p in passports:
    if p.all_required_fields_present():
        passports_with_all_fields +=1
    
valid_passports = 0
for p in passports:
    if p.is_valid():
        valid_passports +=1

print(f"Valid Passports A: {passports_with_all_fields}")
print(f"Valid Passports B: {valid_passports}")