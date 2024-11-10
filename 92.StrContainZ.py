import re
def texMatch(str):
    pattern='\w*Z.\w*'
    if re.search(pattern,str):
        print("Found")
    else:
        print("Not found")    
texMatch("ddfZfdfZ")        