'''

RESERVED WORDS: program, var, end, integer, print

DETECT ERRORS: 
- program (if program is spelled wrong)
- var (if var is spelled wrong)
- begin (if begin is spelled wrong)
- integer (if integer is spelled wrong)
- print (if print is spelled wrong)

UNKNOWN:
- ;     (semicolon is missing if grammar required) 
- '     (comma is missing if grammar required) 
- .     (period is missing if grammar required)   
- (     left parentheses is missing
- )     right parentheses is missing

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