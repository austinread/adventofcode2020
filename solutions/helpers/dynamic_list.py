class DynamicList:
    def __init__(self, default):
        self._array = []
        self.__default = default

    def count(self):
        return len(self._array)
    
    def get_value(self, index):
        index = int(index)
        return self._array[index]

    def set_value(self, index, value):
        index = int(index)

        if self.count() > index:
            self._array[index] = value            
        else:
            for _ in range(self.count(),index+1):
                self._array.append(self.__default)
            self._array[index] = value


class DynamicBinaryListV1(DynamicList):
    def __init__(self, default, default_mask):
        super().__init__(default)
        self.mask = default_mask

    def set_value(self, index, value):
        b = bin(int(value)).replace("0b","")
        if len(b) < len(self.mask):
            b = b.rjust(len(self.mask), "0")

        for c in range(0,len(self.mask)):
            if self.mask[c] != "X":
                b = list(b)
                b[c] = self.mask[c]

        super().set_value(index, ''.join(b))

    def sum_values(self):
        nums = [int(a,2) for a in self._array]
        return sum(nums)

class DynamicBinaryListV2(DynamicList):
    def __init__(self, default, default_mask):
        super().__init__(default)
        self.mask = default_mask

    def set_value(self, index, value):
        b = bin(int(index)).replace("0b","")

        #get masked address with floating bits
        floating_bits = []
        if len(b) < len(self.mask):
            b = b.rjust(len(self.mask), "0")

        for c in range(0,len(self.mask)):
            if self.mask[c] == "X":
                b = list(b)
                b[c] = "X"
                floating_bits.append(c)
            elif self.mask[c] == "1":
                b = list(b)
                b[c] = "1"

        #create a list of binary values, each representing the various combinations of floating bits by themselves
        address_count = pow(2,len(floating_bits))
        character_count = len(bin(address_count-1).replace("0b",""))

        binaries = []
        for i in range(address_count):
            binaries.append(bin(i).replace("0b","").rjust(character_count,"0"))

        #take that list and replace the X's in the address (b), creating a list of addresses to write to
        addresses = []
        for i in range(address_count):
            bit_set = binaries[i]
            for f in range(len(floating_bits)):
                b[floating_bits[f]] = bit_set[f]
            addresses.append(''.join(b))
        
        #finally, update the addresses with the given unchanged value
        for a in addresses:
            decimal_index = int(a,2)
            super().set_value(decimal_index,value)
        

    def sum_values(self):
        return sum(self._array)