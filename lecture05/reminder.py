def get_remainder(x, y):
    # Check for special cases first
    if x == 0 or y == 0 or x == y:
        # If x = 0, remainder is 0
        # If y = 0, normally division by zero is invalid, but here we force remainder = 0
        # If x == y, remainder is 0 because x % y = 0
        remainder = 0
    else:
        # Otherwise, calculate remainder of x divided by y
        # Then divide that remainder by y to get a fractional result
        remainder = (x % y) / y
    return remainder


# Example: 10 % 3 = 1 → 1 / 3 = 0.333...
print(get_remainder(10, 3))   # Output: 0.333333...
