'''

write: print(identifier)    ... DONE
write: print("string", identifier)    ... NEED TO DO

'''

import re
from ppt import check_identifier

def parse_only_id(stat):
    # Use regex to split by '(', ')', and ';', but keep them in the result
    tokens = re.findall(r'print|[();]|\w+', stat)
    print(tokens)
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

def check_string_content(content):
    """Check that the string content inside quotation marks is valid."""
    # Join the list into a single string
    content_str = ''.join(content)

    if '"' not in content_str or content_str.count('"') != 2:
        print("Invalid syntax: Missing or unbalanced quotation marks")
        return False

    # Extract content between quotation marks
    quote_start = content_str.index('"')
    quote_end = content_str.index('"', quote_start + 1)

    # Include everything between and within the quotation marks
    quoted_string = content_str[quote_start + 1:quote_end]

    if not quoted_string.isprintable():
        print("Invalid string inside quotation marks")
        return False

    # Ensure there is a comma right after the closing quotation mark
    if quote_end + 1 >= len(content_str) or content_str[quote_end + 1] != ",":
        print("Invalid syntax: Missing comma after closing quotation mark")
        return False

    after_comma = content_str[quote_end + 2:].strip()
    if not check_identifier(after_comma):
        return False
    
    # print(f"Valid string content: {quoted_string}")
    return True


def parse_with_string(stat):
    """Parse the statement and validate the structure."""
    tokens = re.findall(r'print|[();,"]|(?:\w+|=)', stat)

    # Check for 'print' followed by '('
    if 'print' in tokens:
        print_index = tokens.index('print')
        if print_index + 1 >= len(tokens) or tokens[print_index + 1] != '(':
            print("Invalid syntax: 'print' is not followed by '('")
            return False
    else:
        print("Invalid syntax: Missing 'print'")
        return False

    # Check for ')' followed by ';'
    if ')' in tokens:
        close_paren_index = tokens.index(')')
        if close_paren_index + 1 >= len(tokens) or tokens[close_paren_index + 1] != ';':
            print("Invalid syntax: ')' is not followed by ';'")
            return False
    else:
        print("Invalid syntax: Missing ')'")
        return False

    # Extract and validate content inside parentheses
    if '(' in tokens and ')' in tokens:
        start_index = tokens.index('(')
        end_index = tokens.index(')')
        content_inside_parentheses = tokens[start_index + 1:end_index]
        is_valid = check_string_content(content_inside_parentheses)
        return is_valid
    else:
        print("Invalid syntax: Missing '(' or ')'")
        return False


# Test cases
stat_list_string = [
    'print("value=",2bba);',
    'print("bad example, bba);',
    'print("valid_string=",abc);'
]

for stat in stat_list_string:
    result = parse_with_string(stat)
    print(result)
