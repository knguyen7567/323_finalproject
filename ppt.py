import re

productions = {
    'P': {'program': 'program I ; var DL begin SL end'},
    'I': {
        'a': 'LX',
        'b': 'LX',
        'c': 'LX',
        'd': 'LX',
        'l': 'LX',
        'f': 'LX'
    },
    'X': {
        'a': 'LX',
        'b': 'LX',
        'c': 'LX',
        'd': 'LX',
        'l': 'LX',
        'f': 'LX',
        '0': 'DI X',
        '1': 'DI X',
        '2': 'DI X',
        '3': 'DI X',
        '4': 'DI X',
        '5': 'DI X',
        '6': 'DI X',
        '7': 'DI X',
        '8': 'DI X',
        '9': 'DI X',
        ';': 'λ',
        '=': 'λ',
        ',': 'λ'
    },
    'DL': {
        'a': 'D : TY ;',
        'b': 'D : TY ;',
        'c': 'D : TY ;',
        'd': 'D : TY ;',
        'l': 'D : TY ;',
        'f': 'D : TY ;',
        '0': 'D : TY ;',
        '1': 'D : TY ;',
        '2': 'D : TY ;',
        '3': 'D : TY ;',
        '4': 'D : TY ;',
        '5': 'D : TY ;',
        '6': 'D : TY ;',
        '7': 'D : TY ;',
        '8': 'D : TY ;',
        '9': 'D : TY ;'
    },
    'D': {
        'a': 'I , D',
        'b': 'I , D',
        'c': 'I , D',
        'd': 'I , D',
        'l': 'I , D',
        'f': 'I , D'
    },
    'TY': {'integer': 'integer'},
    'SL': {
        'print': 'S SL',
        'a': 'S SL',
        'b': 'S SL',
        'c': 'S SL',
        'd': 'S SL',
        'l': 'S SL',
        'f': 'S SL',
        'end': 'λ'
    },
    'S': {
        'print': 'W',
        'a': 'A',
        'b': 'A',
        'c': 'A',
        'd': 'A',
        'l': 'A',
        'f': 'A'
    },
    'W': {'print': 'print ( ST I )'},
    'ST': {
        '"value="': '"value=",',
        ';': 'λ',
        '=': 'λ',
        ',': 'λ'
    },
    'A': {
        'a': 'I = E;',
        'b': 'I = E;',
        'c': 'I = E;',
        'd': 'I = E;',
        'l': 'I = E;',
        'f': 'I = E;'
    },
    'E': {
        '(': 'TE\'',
        '+': 'TE\'',
        '-': 'TE\'',
        'a': 'TE\'',
        'b': 'TE\'',
        'c': 'TE\'',
        'd': 'TE\'',
        'l': 'TE\'',
        'f': 'TE\''
    },
    'E\'': {
        '+': '+TE\'',
        '-': '-TE\'',
        ')': 'λ',
        ';': 'λ',
        'end': 'λ'
    },
    'T': {
        '(': 'FT\'',
        '+': 'FT\'',
        '-': 'FT\'',
        'a': 'FT\'',
        'b': 'FT\'',
        'c': 'FT\'',
        'd': 'FT\'',
        'l': 'FT\'',
        'f': 'FT\''
    },
    'T\'': {
        '*': '*FT\'',
        '/': '/FT\'',
        '+': 'λ',
        '-': 'λ',
        ')': 'λ',
        ';': 'λ',
        'end': 'λ'
    },
    'F': {
        '(': '(E)',
        'a': 'I',
        'b': 'I',
        'c': 'I',
        'd': 'I',
        'l': 'I',
        'f': 'I',
        '+': 'N',
        '-': 'N',
        '0': 'N',
        '1': 'N',
        '2': 'N',
        '3': 'N',
        '4': 'N',
        '5': 'N',
        '6': 'N',
        '7': 'N',
        '8': 'N',
        '9': 'N'
    },
    'N': {
        '+': 'SI DI Y',
        '-': 'SI DI Y',
        '0': 'SI DI Y',
        '1': 'SI DI Y',
        '2': 'SI DI Y',
        '3': 'SI DI Y',
        '4': 'SI DI Y',
        '5': 'SI DI Y',
        '6': 'SI DI Y',
        '7': 'SI DI Y',
        '8': 'SI DI Y',
        '9': 'SI DI Y'
    },
    'SI': {
        '+': '+',
        '-': '-',
        ';': 'λ',
        '*': 'λ',
        '/': 'λ',
        'end': 'λ'
    },
    'DI': {
        '0': '0',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9'
    },
    'L': {
        'a': 'a',
        'b': 'b',
        'c': 'c',
        'd': 'd',
        'l': 'l',
        'f': 'f'
    }
}

def tokenize(input_string):
    """
    Tokenizes the input string into meaningful units (tokens).
    """
    # Regular expression to match words, numbers, or special characters
    token_pattern = r'\w+|[^\s\w]'
    return re.findall(token_pattern, input_string)

def parse(input_string):
    tokens = tokenize(input_string)
    tokens.append('$')  # Add end-of-input marker
    print(f"\n\n--------------- Parsing: {input_string} ---------------")
    print(f"Tokens: {tokens}")

    # Initialize stack
    stack = ['$', 'P']
    input_ptr = 0
    read = tokens[input_ptr]

    # Loop to iterate through tokens
    while len(stack) > 0:
        print(f"Stack: {stack}")
        popped = stack.pop()
        print(f"Popped: {popped}")

        # Check if the popped item matches the read token
        if popped == read:
            print(f"\t\t\tMatch: {popped} = {read}")
            input_ptr += 1
            if input_ptr < len(tokens):
                read = tokens[input_ptr]
            continue

        # Look for item based on the predictive parsing table
        if popped in productions:
            if read in productions[popped]:
                prod = productions[popped][read]
                print(f"Production used: {popped} → {prod}")
                
                # Push production in reverse order, ignoring lambda
                if prod != 'λ':
                    for symbol in reversed(prod.split()):  # Split by spaces for multi-character productions
                        stack.append(symbol)
            else:
                print(f"Error: No production for [{popped}, {read}]")
                return False
        else:
            print(f"Error: Unexpected terminal/non-terminal [{popped}]")
            return False

    # Ensure stack is empty and input is completed
    if len(stack) == 0 and input_ptr == len(tokens):
        print("Accepted:", input_string)
        return True
    else:
        print("Rejected:", input_string)
        return False


if __name__ == '__main__':
    input_strings = [
        'program b; var x, y : integer; begin x = 10; y = x + 5; print("value=", y) end',   # VALID
        'program c; var x y : integer; begin print("value=", x) end', # 
        'program a; var a : integer; begin print("value=", a)', # MISSING END
    ]

    for input_str in input_strings:
        parse(input_str)