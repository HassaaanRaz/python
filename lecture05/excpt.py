def main():
    # Call the get_int1() function and print its return value
    # This will keep asking until the user provides a valid integer
    print(get_int1())



# --------------------------------------------------------
# NOTES:
# error: refers to something not working in your code
# syntax error: mistakes in code structure (must be fixed by you before running)
# runtime error: errors that happen when the program is running (e.g., invalid input)
# --------------------------------------------------------

# Example of runtime error handling:
# When entering a string instead of a number,
# the program will catch the ValueError and prompt again.
# Once the user enters a valid integer, the program will continue.


# Generic function to get a number with a custom prompt
def get_number(prompt):
    while True:   # Keep looping until valid input is entered
        try:
            # Try converting input into integer
            return int(input(prompt))
        except ValueError:
            # If conversion fails, show error message and retry
            print("You must enter a number")


# Function that asks specifically for x and handles invalid input
def get_int():
    while True:
        try:
            # Ask for integer input
            x = int(input("what is x:"))
            break   # if successful, exit the loop
        except ValueError:
            # If user enters non-integer, show error message and retry
            print("x is not an integer")
        else:
            # else block runs only if no exception occurred
            break
    return x   # Return the valid integer


# Another version that keeps asking until input is valid
def get_int1():
    while True:
        try:
            # Ask for integer input and return immediately if valid
            return int(input("what is the value of x:"))
        except ValueError:
            # If input is invalid (not an integer), ignore and re-ask
            pass


# Entry point of the program
main()
