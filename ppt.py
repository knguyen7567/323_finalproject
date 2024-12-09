import re

identifier_productions = {
    'I': {  # Start with a letter
        'a': 'LX', 'b': 'LX', 'c': 'LX', 'd': 'LX', 'l': 'LX', 'f': 'LX'
    },
    'X': {  # Continue with letters or digits, or terminate
        'a': 'ZX', 'b': 'ZX', 'c': 'ZX', 'd': 'ZX', 'l': 'ZX', 'f': 'ZX',
        '0': 'ZX', '1': 'ZX', '2': 'ZX', '3': 'ZX', '4': 'ZX', '5': 'ZX',
        '6': 'ZX', '7': 'ZX', '8': 'ZX', '9': 'ZX', ';': 'λ', '=': 'λ', '$': 'λ'
    },
    'L': {  # Match letters
        'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'l': 'l', 'f': 'f'
    },
    'Z': {  # Match digits
        '0': '0', '1': '1', '2': '2', '3': '3', '4': '4',
        '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
        'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'l': 'l', 'f': 'f'
    },
}


def check_identifier(line): 
    if len(line) == 0:
        return False

    stack = ['$','I']  # Start with 'I' for the first letter
    input_ptr = 0
    read = line[input_ptr]

    while len(stack) > 0:
        # print(f"Stack: {stack}")
        popped = stack.pop()
        # print(f"Popped: {popped}")

        # Match terminal symbol
        if popped == read:
            # print(f"\t\t\tMatch: {popped} == {read}")
            input_ptr += 1
            if input_ptr < len(line):
                read = line[input_ptr]
            else:
                read = '$'  # End of input marker
            continue

        # Handle non-terminal symbol
        if popped in identifier_productions:
            if read in identifier_productions[popped]:
                prod = identifier_productions[popped][read]
                # print(f"Applying Production: {popped} -> {prod}")
                
                # Handle lambda
                if prod == 'λ':
                    continue

                # Push production in reverse order
                for symbol in reversed(prod):
                    stack.append(symbol)
            else:
                # print(f"No production for [{popped}, {read}]")
                print(f"Issue with identifier: {line}.")
                return False
        else:
            # print(f"Unexpected symbol: {popped}")
            print(f"Issue with identifier: {line}.")
            return False

    # Final check for acceptance
    if len(stack) == 0 and read == '$':
        # print("Accepted:", line)
        return True
    else:
        # print("Rejected:", line)
        return False

def check_dec_list(declarations, type):
    if type != "integer":
        return False
    
    # checking the identifiers
    for declaration in declarations:
        valid = check_identifier(declaration)
        if valid:
            continue
        else:
            return False

    return True

    
def check_stat(stat): 
    if len(stat) == 0:
        return False

    if 'print' in stat:
        print("write")
    # elif '=' in stat:
    #     print("assign")
    # else:
    #     print("none")
    #     return False
    
    return True

# stat_list = ['a=3;', 'b2a=14;', 'c=5;', 'print(c);', 'bba=a1 * (b2a + 2 * c);', 'print(“value=”,bba);']


def parse(input_dict):

    ''' we want to focus on identifier, dec_list, and stat_list'''

    for k in input_dict:
        if k == 'identifier':
            for a in input_dict['identifier']:
                valid = check_identifier(a)
                if valid:
                    print("~ Identifier is good! Move to dec_list ...")
                    continue
                else:
                    return False
        
        if k == 'dec_list':
            for entry in input_dict['dec_list']:
                # split the declaration by the colon to separate names and type
                parts = entry.split(':')
                if len(parts) == 2:
                    declarations = parts[0].split(',')  # split variable names by commas
                    data_type = parts[1].rstrip(';')   # remove trailing semicolon
                    # print(declarations, data_type)
                    valid = check_dec_list(declarations, data_type)
                    if valid:
                        print("~ dec_list is good! Move to stat_list ...")
                        continue
                    else:
                        return False
                else:
                    print("Error: missing `:`")

        if k == 'stat_list':
            for a in input_dict['stat_list']:
                return

    return True

def valid_input(input_dict):
    if 'program' not in input_dict or not input_dict['program']:
        print('Error with `program` keyword: missing or empty.')
        return False
    if input_dict['program'][0] != 'program':
        print('Error with `program` keyword: incorrect value.')
        return False


    if 'begin' not in input_dict or not input_dict['begin']:
        print('Error with `begin` keyword.')
        return False

    for reserved in input_dict:
        if not input_dict[reserved]:  
            print(f'Missing {reserved}.')
            print(f'If missing is `dec_list`, check spelling of `var`.')
            return False

    if 'end' not in input_dict or not input_dict['end']:
        print('Error with `end` keyword.')
        return False
    
    return True

if __name__ == '__main__':
    input_string = {
        'program' : ['program'],
        'identifier' : ['f2024'],
        ';' : True,
        'var' : True,
        'dec_list' : ['a,b2a,c,bba:integer;'],
        'begin' : True,
        'stat_list' : ['a = 3 ;', 'b2a = 14 ;', 'c = 5 ;', 'print ( c );', 'bba = a1 * ( b2a + 2 * c) ;', 'print ( “value=”, bba ) ;'],
        'end' : True
    }

    is_valid = valid_input(input_string)
    
    if is_valid == False:
        print("Invalid input.")
    else:
        print("Valid Input.")
        parse(input_string)


