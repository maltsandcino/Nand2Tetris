import parser
import coder
import stripper
import symbols
from sys import argv
import pprint as pp

file_path = argv[1]

with open(file_path) as f:
    instructions = [line.rstrip() for line in f]

instructions = stripper.stripping(instructions)

instructions = symbols.convert_symbols(instructions)

pp.pp(instructions)
