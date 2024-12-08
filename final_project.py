from fix_txt import clean

'''

RESERVED WORDS: program, var, end, integer, print

DETECT ERRORS: 
- program (if program is spelled wrong)         ... DONE
- var (if var is spelled wrong)                 ... DONE
- begin (if begin is spelled wrong)             ... DONE
- integer (if integer is spelled wrong)
- print (if print is spelled wrong)

UNKNOWN IDENTIFIER if variable is not defined:
- ;     (semicolon is missing if grammar required) 
- ,     (comma is missing if grammar required) 
- .     (period is missing if grammar required)   
- (     left parentheses is missing
- )     right parentheses is missing

'''

''' PREDICTIVE PARSING TABLE '''

''' [program <identifier> ; var <dec-list> begin <stat-list> end]'''

def parse_program_to_arrays(file_content):
    program_array = []
    identifier_array = []
    dec_list_array = []
    stat_list_array = []
    has_semicolon = False
    has_begin = False
    has_end = False
    current_section = None

    for line in file_content:
        line = line.strip()

        if line.startswith("program"):  # Identify the program and identifier
            parts = line.split()
            program_array.append(parts[0])  # "program"
            identifier_array.append(parts[1].rstrip(";"))  # "f2024"
            has_semicolon = ";" in line  # Check for semicolon

        elif line.startswith("var"):  # Start of declarations
            current_section = "dec_list"

        elif line.startswith("begin"):  # Start of statements
            has_begin = True
            current_section = "stat_list"

        elif line.startswith("end"):  # End of the program
            has_end = True
            break

        elif current_section == "dec_list":  # Add declarations
            dec_list_array.append(line)

        elif current_section == "stat_list":  # Add statements
            stat_list_array.append(line)

    # Prepare the final arrays with the requested structure
    return {
        "program": program_array,
        "identifier": identifier_array,
        ";": ";" if has_semicolon else None,
        "var": "var",
        "dec_list": dec_list_array,
        "begin": "begin" if has_begin else None,
        "stat_list": stat_list_array,
        "end": "end" if has_end else None,
    }



READFILE = 'final.txt'

def execute_program(READFILE):
    cleaned_content = clean(READFILE)
    cleaned_content_array = cleaned_content.split("\n")
    parsed_content = parse_program_to_arrays(cleaned_content_array)

    for key, value in parsed_content.items():
        print(f"{key} = {value}")

execute_program(READFILE)





'''

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

'''

'''

program f2024;
var
a , b2a , c , bba : integer ;
begin
a = 3 ;
b2a = 14 ;
c = 5 ;
print ( c ) ;
bba = ( b2a + 2 * c) * a ;
print ( “Value=” , bba ) ;
end

'''