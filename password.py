user = str(input("")).lower()

if user == "create account":
    uid = str(input("Choose a username\n")).lower()
    passw = str(input("Create a password\n")).lower()
    print("Uid & Password created.")

elif user == "login":
    uid1 = str(input("Enter your username\n")).lower()
    passw1 = str(input("Enter your password\n")).lower()
    uid2 = "shree"
    passw2 = "123"
    if uid1 == uid2 and passw1 == passw2:
        print("Login Sucessfull.")
    else: print("Error! Please try again.")