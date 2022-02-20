user_int = int(input('Enter integer (32 - 126):\n'))
# FIXME (1): Finish reading other items into variables, then output the four values on a single line separated by a space
user_float = float(input('Enter float:\n')) 
user_char = (input('Enter character:\n'))
user_string = (input('Enter string:\n'))
#desired output: 99 3.77 z Howdy
print(user_int,user_float,user_char,user_string)
# FIXME (2): Output the four values in reverse
print(user_string,user_char,user_float,user_int)
# FIXME (3): Convert the integer to a characer, and output that character
user_int_char = chr(user_int)
print(user_int,'converted to a character is',user_int_char)
