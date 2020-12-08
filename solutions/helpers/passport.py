import re

class Passport:
    def __init__(self, raw):
        self.fields = self.parse_raw(raw)
        self.required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    def parse_raw(self, raw):
        raw = raw.replace("\n", " ")
        field_text = raw.split(" ")

        fields = []
        for text in field_text:
            key = text[0:text.index(":")]
            value = text[text.index(":")+1:]
            fields.append(Passport_Field(key, value))

        return fields

    def all_required_fields_present(self):
        valid = True
        for required_field in self.required_fields:
            field_present = False
            for field in self.fields:
                if field.name == required_field:
                    field_present = True
                    break

            if not field_present:
                valid = False
                break

        return valid

    def is_valid(self):
        if not self.all_required_fields_present():
            return False

        valid = True

        for field in self.fields:
            valid = field.is_valid()
            if not valid:
                break

        return valid


class Passport_Field:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def is_valid(self):
        valid = True

        if self.name == "byr":
            valid = len(self.value) == 4 and int(self.value) >= 1920 and int(self.value) <= 2002

        elif self.name == "iyr":
            valid = len(self.value) == 4 and int(self.value) >= 2010 and int(self.value) <= 2020

        elif self.name =="eyr":
            valid = len(self.value) == 4 and int(self.value) >= 2020 and int(self.value) <= 2030

        elif self.name =="hgt":
            measurement = self.value[len(self.value)-2:]

            if measurement != "cm" and measurement != "in":
                return False

            height = self.value[0:len(self.value)-2]
            if not height.isdigit():
                return False
            height = int(height)

            if measurement == "cm" and (height < 150  or height > 193):
                return False

            if measurement == "in" and (height < 59  or height > 76):
                return False
        
        elif self.name =="hcl":
            if len(self.value) != 7:
                return False

            if self.value[0] != "#":
                return False

            regex = re.compile("^[a-fA-F0-9_]*$")
            if  not regex.match(self.value[1:]):
                return False

            return True

        elif self.name =="ecl":
            valid_eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            valid = valid_eye_colors.__contains__(self.value)

        elif self.name =="pid":
            valid = len(self.value) == 9 and self.value.isdigit()
            
        return valid