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