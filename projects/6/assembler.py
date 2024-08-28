from parser import Parser
from coder import Coder
import stripper
import symbols
from sys import argv
import pprint as pp

def main():
    parser = Parser()
    coder = Coder()

    file_path = argv[1]

    if len(argv) != 2 or not argv[1].endswith(".asm"):
        print("Usage: python assembler.py path_to_file.asm")
        return 1

    with open(file_path) as f:
        instructions = [line.rstrip() for line in f]

    instructions = stripper.stripping(instructions)

    instructions = symbols.convert_symbols(instructions)

    instructions = parser.parse_instructions(instructions)

    instructions = coder.convert(instructions)

    file_path = file_path[:-4] + ".hack"

    with open(file_path, 'w') as f:
        for command in instructions:
            f.write(command + '\n')
    print("Your file has been successfully assembled into machine language")

if __name__ == "__main__":
    main()

