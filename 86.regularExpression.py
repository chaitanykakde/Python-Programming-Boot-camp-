#match(pattern,string) -Beggining of the string
import re
string="She sells ses shells on the sea shore"
pattern="She"
if re.match(pattern,string):
    print("Match found")
else:
    print("Match Not found")

