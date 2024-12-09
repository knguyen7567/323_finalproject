'''
ORIGINAL:

program f2024;
(* This program computes and prints the value
of an expression *)
var
(* declare variables *)
a ,    b2a ,    c, bba  : integer ;
begin
    a           = 3 ;
    b2a =        14 ;
    c            = 5 ;
print ( c ); (* display c *)

    (* compute the value of the expression *)
    bba = a1 * ( b2a + 2 * c)     ;
    print ( “value=”,      bba ) ; (* print the value of bba*)

end
'''

content = None

def clean(FILENAME):
    with open(FILENAME, encoding='utf-8') as f:
        content = f.read()
    
    cleaned_content = []
    inside_comment = False
    
    for line in content.splitlines():
        line = line.strip()
        
        # handle multi-line comments
        if "(*" in line and "*)" in line:
            # remove everything between '(*' and '*)' in the same line
            line = line.split("(*")[0] + line.split("*)")[-1]
        elif "(*" in line:
            # start of a multi-line comment
            inside_comment = True
            line = line.split("(*")[0]
        elif "*)" in line:
            # end of a multi-line comment
            inside_comment = False
            line = line.split("*)")[-1]
        elif inside_comment:
            # skip lines inside multi-line comments
            continue
        
        # process non-empty lines
        if line:
            line = ' '.join(line.split())  # Normalize spaces
            cleaned_content.append(line)
    
    # join the cleaned lines with a newline
    cleaned_code = "\n".join(cleaned_content)
    
    # fix spacing around symbols
    cleaned_code = cleaned_code.replace(" ,", ",").replace(', ', ',')
    cleaned_code = cleaned_code.replace(" : ", ":")
    cleaned_code = cleaned_code.replace(" ;", ";")
    cleaned_code = cleaned_code.replace("= ", "=")
    cleaned_code = cleaned_code.replace(" =", "=")
    cleaned_code = cleaned_code.replace("( ", "(").replace(" )", ")")
    cleaned_code = cleaned_code.replace("print (", "print(")
    
    return cleaned_code

def read(file):
    with open('final.txt', encoding='utf-8') as f:
        content = f.read()
        return content

if __name__ == '__main__':
    content = read('final.txt')
    cleaned_content = clean(content)
    print(cleaned_content)