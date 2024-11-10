import re
def matching(text):
    pattern='^[A-Za-z_0-9]*$'
    if re.search(pattern,text):
        print("Found a match")
    else:
        print("Not found a match")    
matching("HELnnLO777_")        