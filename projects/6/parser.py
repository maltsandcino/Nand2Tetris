'''
This is used to convert C strings to Individual Parts, which will then be converted to machine-code using the tables

'''
import re
    
def dtoB(decimal_number):
    
    num = f'{decimal_number:16b}'
    
    return num

class Parser:

    def parse_instructions(self, instructions: list) -> list:

        for i, line in enumerate(instructions):
            if line[0] == "@":
                num = int(line[1:])
                if num >= 0:
                    num = bin(num)
                    num = num[2:].zfill(16)
                else:
                    pass
                instructions[i] = [num]
                continue
            if "=" in line:
                index = line.find("=")
                dest = line[:index]
                comp = line[(index + 1):]
                jump = None
                instructions[i] = ["111", comp, dest, jump]
            elif ";" in line:
                index = line.find(";")
                dest = None
                comp = line[:index]
                jump = line[(index + 1):]
                instructions[i] = ["111", comp, dest, jump]

        return instructions