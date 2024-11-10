import re
def match(text):
    pattern='ab{3}?'
    if re.search(pattern,text):
        print("Found a match")
    else:
        print("Not Match") 
match("3jdddabbbdjkla");           
