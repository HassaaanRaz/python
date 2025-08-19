

def main():
    x = int(input("Enter an integer: "))

    if is_even(x):
        print(f"{x} is even.")
    else:
        print(f"{x} is odd.")
        

def is_even(n):
    """Check if a number is even."""
    return n % 2 == 0



main()