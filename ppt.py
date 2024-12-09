productions = {

}

def check_identifier(line): 
    return

def parse(input_dict):

    ''' we want to focus on identifier, dec_list, and stat_list'''

    for k in input_dict:
        if k == 'identifier':
            for a in input_dict['identifier']:
                valid = check_identifier(a)
                if valid:
                    continue
                else:
                    return False
        
        if k == 'dec_list':
            for a in input_dict['dec_list']:
                return
        
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
        'dec_list' : ['a , b2a , c, bba : integer ;'],
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