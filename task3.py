#!python3

"""
Create a function called title that creates a single line of output to display the word
"Title" with a box around it.  
The function will have 1 optional input:
symbol : string.  The symbolt to use as the border. Default symbol is "="

The return value is the output string with escaped line breaks.

example assertion:
assert title("*") == "*********\n* Title *\n*********"
assert title() == "=========\n= Title =\n========="
(2 points)

"""
def title(symbol = "="):
    x = (str(symbol)*9 + "\n" + str(symbol)* 1 + " Title " + str(symbol)* 1 + "\n" + str(symbol)*9)
    return x
result = title() 
assert title("*") == "*********\n* Title *\n*********"
assert title() == "=========\n= Title =\n========="