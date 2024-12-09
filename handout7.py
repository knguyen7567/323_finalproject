def parse(input_string):
    print(f"\n\n--------------- Parsing: {input_str} ---------------")

    productions = {
        'S': {'a': 'aW'},
        'W': {'=': '=E'},
        'E': {'a': 'TQ', 'b': 'TQ', '(': 'TQ'},
        'Q': {'+': '+TQ', '-': '-TQ', ')': 'λ', '$': 'λ'},
        'T': {'a': 'FR', 'b': 'FR', '(': 'FR'},
        'R': {'+': 'λ', '-': 'λ', '*': '*FR', '/': '/FR', ')': 'λ', '$': 'λ'},
        'F': {'a': 'a', 'b': 'b', '(': '(E)'}
    }

    # initialize stack
    stack = ['$','S']
    input_ptr = 0
    read = input_string[input_ptr]

    # loop to iterate through input_string
    while len(stack) > 0:
        print(f"Stack: {stack}")
        popped = stack.pop()
        print(f"Popped: {popped}")


        # check for the read item and print if the popped item is the same as the read item
        if popped == read:
            print(f"\t\t\tMatch: [{popped}, {prod}] = {read}")
            input_ptr += 1
            if input_ptr < len(input_string):
                read = input_string[input_ptr]
            continue

        # look for item based on the predictive parsing table
        if popped in productions and read in productions[popped]:
            prod = productions[popped][read]
            
            # continue to the next without pushing to stack if lambda
            if prod != 'λ':
                for symbol in prod[::-1]: # push productions in reverse
                    stack.append(symbol)
        else:
            print(f"No production for [{popped}, {prod}] = {read}")
            continue

    # ensure stack is empty and input is completed
    if len(stack) == 0 and input_ptr == len(input_string):
        print("Accepted:", input_string)
        return True
    else:
        print("Rejected:", input_string)
        return False


if __name__ == '__main__':
    input_strings = [
        "a=(a+b)*a$",
        "a=a*(b-a)$",
        "a=(a+a)b$"
    ]

    for input_str in input_strings:
        parse(input_str)