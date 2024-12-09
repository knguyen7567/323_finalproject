from fix_txt import clean
from ppt import valid_input, parse

'''

RESERVED WORDS: program, var, end, integer, print

DETECT ERRORS: 
- program (if program is spelled wrong)         ... DONE
- var (if var is spelled wrong)                 ... DONE
- begin (if begin is spelled wrong)             ... DONE
- integer (if integer is spelled wrong)         ... DONE
- print (if print is spelled wrong)

UNKNOWN IDENTIFIER if variable is not defined:
- ;     (semicolon is missing if grammar required)         ... DONE
- ,     (comma is missing if grammar required) 
- .     (period is missing if grammar required)   
- (     left parentheses is missing
- )     right parentheses is missing

'''

def parse_program_to_arrays(file_content):
    program_array = []
    identifier_array = []
    dec_list_array = []
    stat_list_array = []
    has_semicolon = False
    has_begin = False
    has_end = False
    has_var = False
    current_section = None

    for line in file_content:
        line = line.strip()

        if line.startswith("program"):  # Identify the program and identifier
            parts = line.split()
            program_array.append(parts[0])  # "program"
            identifier_array.append(parts[1].rstrip(";"))  # "f2024"
            has_semicolon = ";" in line  # Check for semicolon

        elif line.startswith("var"):  # Start of declarations
            has_var = True
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
        ";": True if has_semicolon else False,
        "var": True if has_var else False,
        "dec_list": dec_list_array,
        "begin": True if has_begin else False,
        "stat_list": stat_list_array,
        "end": True if has_end else False,
    }

READFILE = 'final.txt'

'''

Based on the the notes, the structure of an input should be like this:

    program <identifier> ; var <dec-list> begin <stat-list> end

    example:
        program = ['program']
        identifier = ['f2024']
        ; = 
        var = True
        dec_list = ['a , b2a , c, bba : integer ;']
        begin = begin
        stat_list = ['a = 3 ;', 'b2a = 14 ;', 'c = 5 ;', 'print ( c );', 'bba = a1 * ( b2a + 2 * c) ;', 'print ( “value=”, bba ) ;']
        end = end

With that being said. The project functions in a few steps.

    1. Cleans the final.txt file and removes comments and indentations, extra spaces, etc ......'cleaned_content'
    2. Convert cleaned file into an array  ...... 'clean_content_array'
    3. Format the array into a dictionary that helps our program interpret it easier ...... 'parsed_content'

        i.      program : ['program']
        ii.     identifier : ['f2024']
        iii.    ; : True
        iv.     var : True
        v.      dec_list : ['a, b2a, c, bba : integer;']
        vi.     begin : True
        vii.    stat_list : ['a=3;', 'b2a=14;', 'c=5;', 'print (c);', 'bba=a1 * (b2a + 2 * c);', 'print (“value=”, bba);']
        viii.   end : True

    4. This makes sure that the keywords and semicolons are in the proper order even before checking the identifiers in our program.
    5. Check identifier, dec_list, and stat_list.
    
'''

def execute_program(READFILE):
    cleaned_content = clean(READFILE)
    cleaned_content_array = cleaned_content.split("\n")
    parsed_content = parse_program_to_arrays(cleaned_content_array)

    # Uncomment the lines below for debugging
    for k, v in parsed_content.items():
        print(f'{k} : {v}')

    is_valid = valid_input(parsed_content)
    
    if is_valid == False:
        print("~ Invalid input format ...")
    else:
        print("~ Valid input format ...")
        parse(parsed_content)
    


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