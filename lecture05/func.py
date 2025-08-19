def main():
    # Ask the user for a string input using get_str()
    x = get_str("what is x: ")
    
    # Print the value of x back to the user
    print(f"x is {x}")


def get_int(prompt):
    """
    Function to safely get an integer input from the user.
    Keeps asking until the user types a valid integer.
    """
    while True:
        try:
            # Try converting input into an integer
            return int(input(prompt))
        except ValueError:
            # If conversion fails (e.g., user typed "abc"), try again
            pass


def get_str(prompt):
    """
    Function to get a string input from the user.
    Since input() always returns a string, this will always succeed.
    The try-except block is unnecessary, but included
    for consistency with get_int().
    """
    while True:
        try:
            # input() always returns a string, so this will always work
            return input(prompt)
        except ValueError:
            # This will never actually run, but left for symmetry
            pass


# Call main function directly when script runs
main()
