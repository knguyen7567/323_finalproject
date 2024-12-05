from fix_txt import clean

# Clean the content and execute the program
READFILE = 'final.txt'

cleaned_content = clean(READFILE)
cleaned_content_to_array = cleaned_content.split("\n")

def execute_program(cleaned_content):
    print(cleaned_content_to_array)

    # Initialize variables
    pl = 0
    q2s = 0
    r = 0
    pp = 0

    # Split the cleaned content into individual lines
    program_lines = cleaned_content.split('\n')

    # Execute each line of the program
    for line in program_lines:
        # Remove leading and trailing whitespace
        line = line.strip()

        # Skip empty lines
        if not line:
            continue

        # Separate the instruction and its arguments
        parts = line.split(' ', 1)
        instruction = parts[0]
        args = parts[1] if len(parts) > 1 else ''

        # Strip off non-numeric characters from the arguments
        args = ''.join(filter(str.isdigit, args))

        # Execute the instruction based on its type
        if instruction == 'program':
            pass  # Ignore program declaration
        elif instruction == 'var':
            pass  # Ignore variable declaration
        elif instruction == 'begin':
            pass  # Ignore begin statement
        elif instruction == 'end':
            break  # End of program
        elif instruction == 'pl=':
            pl = int(args)
        elif instruction == 'pp=':
            pp = int(args)
        elif instruction == 'q2s=':
            q2s = int(args)
        elif instruction == 'r=':
            r = int(args)
        elif instruction == 'write(p1);':
            print("Value of p1:", pl)
        elif instruction == 'write("value=", pp );':
            print("Value of pp:", pp)
        else:
            # Handle other instructions if needed
            pass

execute_program(cleaned_content)