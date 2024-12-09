'''

write: print(identifier)

'''

import re
from ppt import check_identifier

def parse(stat):
    # Use regex to split by '(', ')', and ';', but keep them in the result
    tokens = re.findall(r'print|[();]|\w+', stat)
    
    if 'print' in tokens:
        print_index = tokens.index('print')
        if print_index + 1 >= len(tokens) or tokens[print_index + 1] != '(':
            return False  # 'print' is not followed by '('
    else: 
        return False

    if ')' in tokens:
        close_paren_index = tokens.index(')')
        if close_paren_index + 1 >= len(tokens) or tokens[close_paren_index + 1] != ';':
            return False  # ')' is not followed by ';'

    if '(' in tokens and ')' in tokens:
        start_index = tokens.index('(')
        end_index = tokens.index(')')
        content_inside_parentheses = tokens[start_index + 1:end_index]

        valid_identifier = check_identifier(content_inside_parentheses[0])
        if valid_identifier:
            return True
        else:
            return False
    else:
        return False

stat_list = ['print(c);', 'print(bba);']

for stat in stat_list:
    result = parse(stat)
    print(result)
