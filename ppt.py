import re
from handle_print import parse_with_string, parse_only_id
from handle_identifier import check_identifier
from handle_assign import handle_assign

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

    if 'print' and '"' in stat:
        # print("write with string")
        valid = parse_with_string(stat)
        return True if valid else False
    elif 'print' in stat:
        # print("write no string")
        valid = parse_only_id(stat)
        return True if valid else False
    elif '=' in stat and 'print' not in stat:
        # print(f'assign: {stat}')
        valid = handle_assign(stat)
        return True if valid else False
    
    else:
        # print("something is likely mispelled")
        return False
    

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
                # print(a)
                valid = check_stat(a)
                # print(f'{a} is {valid}')
                if valid:
                    continue
                else:
                    return False
            print("~ stat_list is good! Move to end ...")

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
        'stat_list' : ['a=3;', 'b2a=14;', 'c=5;', 'print(c);', 'bba=a1*(b2a+2*c);', 'print("value=",bba);'],
        'end' : True
    }

    is_valid = valid_input(input_string)
    
    if is_valid == False:
        print("Invalid input.")
    else:
        print("~ Valid Input format!")
        parse(input_string)


