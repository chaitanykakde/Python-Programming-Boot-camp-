# matchList=re.find
# (pattern,input_str,flags=0)
import re
pattern=r"[a-zA-Z]+ \d+"
input_str="ii 2023,VXI 2015 ,VDI 2014,Maruti Suzuki cars in India"
matches=re.findall(pattern,input_str)
for i in matches:
    print(i," ")