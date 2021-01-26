class Conversion():
    decimal_conversion = {
        '0': ['0000', '0', '0'],
        '1': ['0001', '1', '1'],
        '2': ['0010', '2', '2'],
        '3': ['0011', '3', '3'],
        '4': ['0100', '4', '4'],
        '5': ['0101', '5', '5'],
        '6': ['0110', '6', '6'],
        '7': ['0111', '7', '7'],
        '8': ['1000', '10', '8'],
        '9': ['1001', '11', '9'],
        '10': ['1010', '12', 'A'],
        '11': ['1011', '13', 'B'],
        '12': ['1100', '14', 'C'],
        '13': ['1101', '15', 'D'],
        '14': ['1110', '16', 'E'],
        '15': ['1111', '17', 'F'],
    }
    def hexToBinary(self, hex_num: str) -> str:
        bin_num = []
        for hex_digit in hex_num:
            bin_num.append(self.findConversion(hex_digit, 2))
        return ''.join(bin_num)

    def binaryToHex(self, bin_num: str) -> str:
        seperated_bin_num = []
        hex_num = []
        if len(bin_num) % 4 != 0:
            bin_num.zfill(4 - (len(bin_num) % 4))
        for num in range(0, len(bin_num), 4):
            seperated_bin_num.append(bin_num[num:num+4])
        for binary in seperated_bin_num:
            hex_num.append(self.findConversion(binary, 16))
        return ''.join(hex_num)

    def binaryToOctal(self, bin_num: str) -> str:
        oct_num = []
        seperated_bin_num = []
        if len(bin_num) % 4 != 0:
            bin_num.zfill(4 - (len(bin_num) % 4))
        for num in range(0, len(bin_num), 4):
            seperated_bin_num.append(bin_num[num:num+4])
        for binary in seperated_bin_num:
            oct_num.append(self.findConversion(binary, 8))
        return ''.join(oct_num)

    def octalToBinary(self, oct_num: str) -> str:
        bin_num = []
        for oct_digit in oct_num:
            bin_num.append(self.findConversion(oct_digit, 2))
        return ''.join(bin_num)

    def hexToOctal(self, hex_num: str) -> str:
        oct_num = []
        for hex_digit in hex_num:
            oct_num.append(self.findConversion(hex_digit, 8))
        return ''.join(oct_num)
    
    def octalToHex(self, oct_num: str) -> str:
        hex_num = []
        for oct_digit in oct_num:
            hex_num.append(self.findConversion(oct_digit, 16))
        return ''.join(hex_num)

    def binaryToDecimal(self, bin_num: str) -> str:
        return self.anyToDecimal(bin_num, 2)

    def decimalToBinary(self, dec_num: str) -> str:
        return self.decimalToAny(dec_num, 2)

    def hexToDecimal(self, hex_num: str) -> str:
        return self.anyToDecimal(hex_num, 16)

    def decimalToHex(self, dec_num: str) -> str:
        return self.decimalToAny(dec_num, 16)

    def octalToDecimal(self, oct_num: str) -> str:
        return self.anyToDecimal(oct_num, 8)

    def decimalToOctal(self, dec_num: str) -> str:
        return self.decimalToAny(dec_num, 8)

    def anyToDecimal(self, num: str, base: str) -> str:
        dec_num = 0
        for index in range(0, len(num)):
            dec_num += num[(index * -1) - 1] * base**index
        return f'{dec_num}'

    def decimalToAny(self, dec_num: str, base: str) -> str:
        return ''

    def findConversion(self, num: str, base: int) -> str:
        """ Finds the number for a requested number base
            based on what's in the decimal conversion
            dictionary

            Parameters
            ----------
            num : str - 
              the number in the number base you are 
              converting from
            
            base: int -
              the number base you are converting to
            
            Returns
            -------
            str -
              the number in the requested base that 
              matches the original number
        """
        list_index = 0
        if base == 2:
            list_index = 0
        elif base == 8:
            list_index = 1
        elif base == 16:
            list_index = 2
        for index, values in enumerate(self.decimal_conversion):
            if num in values:
                return self.decimal_conversion[f'{index}'][list_index]