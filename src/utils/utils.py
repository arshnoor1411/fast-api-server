import math, random

async def generate_otp():
    print('OTP function')
    string = '0123456789'
    OTP = ""
    length = len(string)
    for i in range(6) :
        OTP += string[math.floor(random.random() * length)]
 
    print("KKK",OTP)
    return OTP