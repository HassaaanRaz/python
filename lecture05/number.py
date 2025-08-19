    
try:
    x = int(input("what's x?"))
# if someone add a str the systems throws and error

except ValueError:
    print("you must enter a number")

else:
    print(f"x is {x}")

#print(f"x is {x}")
#this error is due to the fact that int() don't accept strings
