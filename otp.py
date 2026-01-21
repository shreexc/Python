import random

otp = random.randint(999, 9999)
print(otp)

user = int(input("Enter the OTP:\n> "))

if user == otp:
    print("OTP verified successfully.")
else: print("Error! Please try again.")