'''
This is used to convert C strings to Individual Parts, which will then be converted to machine-code using the tables

'''
import re

instruction_table = {"0": "0101010", "1": "0111111", "-1": "0111010", "D": '0001100', "A": "0110000", "!D": "0001101", "!A": "0110001", "-D": "0001111", "-A": "0110011",
                     "D+1": "0011111"

}

jump_table = {

}

destination_table = {

}

def parse_instructions(instructions: list) -> list:

    return instructions