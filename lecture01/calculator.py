# calculator.py

#this will take two numbers from the user and calculate their sum
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

# Convert inputs to float for more general use
a = float(input("Enter a number: "))
b = float(input("Enter another number: "))

# Calculate the sum of x and y
z = x + y

# Calculate the sum of a and b
c = round(a + b)

# Print the result 
print("The sum of x and y is:", z)

#better way to print the result
print("The sum of x and y is:",x + y)



# Print the result 
print("The sum of a and b is:", c)

#better way to print the result
print("The sum of a and b is:",c)


# Print the result with formatted output
print(f"The sum of a and b is: {c:,}")