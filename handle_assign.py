import re
from handle_identifier import check_identifier

productions = {
    'E': {
        'a': 'TA', 'b': 'TA', 'c': 'TA', 'd': 'TA', 'l': 'TA', 'f': 'TA', 
        '+': 'TA', '-': 'TA', '(': 'TA', '0': 'TA', '1': 'TA', '2': 'TA', 
        '3': 'TA', '4': 'TA', '5': 'TA', '6': 'TA', '7': 'TA', '8': 'TA', 
        '9': 'TA'
    },
    'A': {
        '+': '+TA', '-': '-TA', ')': 'λ', '$': 'λ', ';': 'λ'
    },
    'T': {
        'a': 'FB', 'b': 'FB', 'c': 'FB', 'd': 'FB', 'l': 'FB', 'f': 'FB', 
        '+': 'FB', '-': 'FB', '(': 'FB', '0': 'FB', '1': 'FB', '2': 'FB', 
        '3': 'FB', '4': 'FB', '5': 'FB', '6': 'FB', '7': 'FB', '8': 'FB', 
        '9': 'FB', ';': 'λ'
    },
    'B': {
        '*': '*FB', '/': '/FB', '+': 'λ', '-': 'λ', ')': 'λ', '$': 'λ', ';': 'λ'
    },
    'F': {
        'a': 'I', 'b': 'I', 'c': 'I', 'd': 'I', 'l': 'I', 'f': 'I',
        '+': 'N', '-': 'N', '(': '(E)', '0': 'N', '1': 'N', '2': 'N', 
        '3': 'N', '4': 'N', '5': 'N', '6': 'N', '7': 'N', '8': 'N', 
        '9': 'N', ';': 'λ'
    },
    'I': {
        'a': 'LX', 'b': 'LX', 'c': 'LX', 'd': 'LX', 'l': 'LX', 'f': 'LX', ';': 'λ'
    },
    'X': {
        'a': 'LX', 'b': 'LX', 'c': 'LX', 'd': 'LX', 'l': 'LX', 'f': 'LX', 
        '0': 'DX', '1': 'DX', '2': 'DX', '3': 'DX', '4': 'DX', '5': 'DX', 
        '6': 'DX', '7': 'DX', '8': 'DX', '9': 'DX', '+': 'λ', '-': 'λ', 
        ')': 'λ', '$': 'λ', ';': 'λ'
    },
    'N': {
        '+': 'XDY', '-': 'XDY', '0': 'XDY', '1': 'XDY', '2': 'XDY', 
        '3': 'XDY', '4': 'XDY', '5': 'XDY', '6': 'XDY', '7': 'XDY', 
        '8': 'XDY', '9': 'XDY', ';': 'λ'
    },
    'Y': {
        '0': 'DY', '1': 'DY', '2': 'DY', '3': 'DY', '4': 'DY', '5': 'DY', 
        '6': 'DY', '7': 'DY', '8': 'DY', '9': 'DY', '+': 'λ', '-': 'λ', 
        ')': 'λ', '$': 'λ'
    },
    'D': {
        '0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', 
        '6': '6', '7': '7', '8': '8', '9': '9'
    },
    'L': {
        'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'l': 'l', 'f': 'f'
    }
}

def valid_parenthesis(expr):
    stack = []  # Stack to keep track of opening parentheses
    
    # Dictionary to map closing parentheses to their corresponding opening ones
    matching_parentheses = {')': '(', '}': '{', ']': '['}
    
    for char in expr:
        # If the character is an opening parenthesis, push it to the stack
        if char in '({[':
            stack.append(char)
        # If the character is a closing parenthesis, check for a match
        elif char in ')}]':
            if not stack or stack[-1] != matching_parentheses[char]:
                return False  # Unmatched or misplaced closing parenthesis
            stack.pop()  # Pop the matching opening parenthesis from the stack

    # If the stack is empty, all parentheses were matched correctly
    return len(stack) == 0

def parse_expr(expr):
    # print(f"\n\n--------------- Parsing: {expr} ---------------")
    stack = ['$','E']
    input_ptr = 0
    read = expr[input_ptr]

    # loop to iterate through input_string
    while len(stack) > 0:
        # print(f"Stack: {stack}")
        popped = stack.pop()
        # print(f"Popped: {popped}")


        # check for the read item and print if the popped item is the same as the read item
        if popped == read:
            # print(f"\t\t\tMatch: [{popped}, {prod}] = {read}")
            input_ptr += 1
            if input_ptr < len(expr):
                read = expr[input_ptr]
            continue

        # look for item based on the predictive parsing table
        if popped in productions and read in productions[popped]:
            prod = productions[popped][read]
            
            # continue to the next without pushing to stack if lambda
            if prod != 'λ':
                for symbol in prod[::-1]: # push productions in reverse
                    stack.append(symbol)
            
        if popped == '$' and read == ';':
            # print(f"\t\t\tMatch: [End of Input] = {read}")
            break
        else:
            # print(f"No production for [{popped}, {prod}] = {read}")
            continue

    # ensure stack is empty and input is completed
    # print(stack, input_ptr, len(expr))
    if len(stack) == 0 and input_ptr == len(expr)-1:
        # print("Accepted:", expr)
        return True
    else:
        print("Rejected expression:", expr)
        return False


def handle_assign(assignment):
    if assignment.count('=') != 1:
        return False
    
    left_identifier, right_side = assignment.split('=')
    left_identifier = left_identifier.strip()
    right_side = right_side.strip()

    left_valid = check_identifier(left_identifier)

    if not left_valid:
        print('Invalid left identifier.')
        return False
    if right_side[-1] != ';':
        print('Missing semicolon and end of assignment.')
        return False
    if not valid_parenthesis(right_side):
        print("Invalid parenthesis.")
        return False
    
    right_valid = parse_expr(right_side)
    if right_valid:
        # print("~ Expression is valid!")
        return True
    else:
        return False
    # print(right_valid)
    

testcases = ['bba=a1*(b2a+2*c);']

for testcase in testcases:
    valid = handle_assign(testcase)




'''

E -> TA;
A -> +TA
A -> -TA
A -> lambda

T -> FB
B -> *FB
B -> /FB
B -> lambda

F -> I
F -> N
F -> (E)

I -> LX
X -> LX
X -> DX
X -> lambda

N -> XDY
Y -> DY
Y -> lambda
X -> +
X -> -
X -> lambda

D -> 0 | 1 | 2 | ... | 9
L -> a | b | c | d | l | f

'''