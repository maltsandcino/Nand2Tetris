symbol_table = {
    "R0": 0, "R0": 1,"R0": 2, "R0": 3, "R0": 4, "R0": 5, "R0": 6, "R0": 7,
    "R0": 8, "R0": 9, "R0": 10, "R0": 11, "R0": 12, "R0": 13, "R0": 14, "R15": 15,
    "SCREEN": 16384, "KBD": 24576, "SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4,
}

def convert_symbols(instructions: list) -> list:

    instruction_number = 0
    first_available_slot = 16

    # Handling Labels
    for i, line in enumerate(instructions):
        if line[0] == "(":
            temp_symbol = line[1:-1]
            if temp_symbol not in symbol_table:
                symbol_table[temp_symbol] = instruction_number


    # Handling either A Instructions (do nothing besides increment the instructions) or variable declaration/use
        if line[0] == '@':
            temp_symbol = line[1:]
            if temp_symbol.isdigit():
                instruction_number += 1
                continue

    # If present, just grab the value from the table
            if temp_symbol in symbol_table:
                instructions[i] = f"@{symbol_table[temp_symbol]}"
    
    # If not present in table, find the first available RAM slot we can use by looking at the values in the table, and assign that to the NEW symbol.
            if temp_symbol not in symbol_table:
                while first_available_slot in symbol_table.values():
                    first_available_slot += 1
                symbol_table[temp_symbol] = first_available_slot
                instructions[i] = f"@{first_available_slot}"

    # Increment Instructions (We need do do this to keep track of labels)
            instruction_number += 1
        
        else:
            instruction_number += 1

    instructions = [line for line in instructions if line[0] != '(']
    return instructions
