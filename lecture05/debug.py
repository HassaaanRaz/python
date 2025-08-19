def main():
    # Ask user for height of the pyramid (integer only)
    height = get_int("Height: ")
    
    # Call pyramid() to draw with given height
    pyramid(height)


def pyramid(n):
    """
    Draws a simple pyramid-like pattern using '#'.
    n = number of rows (height of pyramid).
    """
    # Loop from 0 up to n-1
    for i in range(n):
        # Print the loop index i (for debugging/understanding),
        # 'end = " "' keeps it on the same line
        print(i, end=" ")
        
        # Print i '#' symbols on the same line
        # Multiplying string '#' by i repeats it i times
        print("#" * i)


def get_int(prompt):
    """
    Safely ask for an integer input.
    Keeps prompting until user enters a valid integer.
    """
    while True:
        try:
            return int(input(prompt))  # Try converting input to int
        except ValueError:
            # If input isn't an integer (e.g., "abc"), ask again
            pass


# Debug tip: You can put a breakpoint inside pyramid() at:
#   print(i, end=" ")
# to check values of i and how '#' * i grows each iteration.

# Run only when executed directly
if __name__ == "__main__":
    main()
