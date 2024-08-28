'''

This will convert parsed c command elements to machine language

'''
import tables

ins_table = tables.instruction_table
jmp_table = tables.jump_table
dest_table = tables.destination_table

command = 1
destination = 2
jump_condition = 3

class Coder:

    def convert(self, instructions: list) -> list:

        for i, line in enumerate(instructions):
            if len(line) > 1:
                if line[command] in ins_table:
                    instructions[i][command] = ins_table[line[command]]

                if line[destination] in dest_table:
                    instructions[i][destination] = dest_table[line[destination]]

                if line[jump_condition] in jmp_table:
                    instructions[i][jump_condition] = jmp_table[line[jump_condition]]
            
            instructions[i] = "".join(instructions[i])


        return instructions

