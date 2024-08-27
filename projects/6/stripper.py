import copy
"""
Used to remove non-instruction / label lines from program

"""

def stripping(instructions):
    ins = instructions.copy()
    sec = []
    
    starting_symbols = [
        '(',
        '@',
        '',
        '/',
        '\n',
        '\r',
        'D',
        'M',
        'A',
        '0',
        '-',
        '1',
        '!'
    ]

    for line in instructions:
        
        if len(line) > 0 and line[0] not in starting_symbols:
            print(line)
            return ValueError("Line beginning with non-comment or instruction")

    for i, line in enumerate(instructions):
        if "//" in line:
            index = line.find("/")
            ins[i] = line[:index]

    for i, line in enumerate(ins):
        if line == "":
            sec.append(line)
    
    sublist_len = len(sec)
    for i in range(len(ins) - sublist_len + 1):
        if ins[i:i + sublist_len] == sec:
            del ins[i:i + sublist_len]
            break
    
    return ins
        