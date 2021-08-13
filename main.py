import os,math
import random,sys
import smtplib

## generating random number and storing it in variable##
digits="0123456789"
otp=""
for i in range(6):
    otp=otp+digits[math.floor(random.random()*10)]

otps=otp+ " is your OTP"
msg=otps

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("singh235shubham@gmail.com", "zavtwjaolcacnfjy")
emailid = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&',emailid,msg)
a = input("Enter Your OTP >>: ")
if a == otp:
    print("Verified")
else:
    print("Please Check your OTP again")


os.system('python OTP-checker.py')
