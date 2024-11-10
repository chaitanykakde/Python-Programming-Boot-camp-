#sub(pattern,repl,string,max=0) -sReplace specified string
import re
string="She sells sea shells on the sea shore sea sea sea"
pattern="sea"
replace="Ocean"
new_str=re.sub(pattern,replace,string,0)
print('New String:',new_str)



