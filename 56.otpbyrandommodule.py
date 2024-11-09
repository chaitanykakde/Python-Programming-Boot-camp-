import random,math
def generateOTP():
    digits="0123456789"
    OTP=" "
    for i in range(1,7):
       a=random.random()
       b=math.floor(a*10)
       OTP+=str(b)
    return OTP   

print("OTP:",generateOTP())