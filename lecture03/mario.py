def main():
    # Get the size of the square from the user
    row, column = sq_size()
    print_square(row, column)
    

# Function to get the size of the square
# It will return the number of rows and columns
def sq_size():
    row = get_inp("Enter the number of rows: ")
    column = get_inp("Enter the number of columns: ")
    return row, column


# Function to print a column of hashes
def print_column(height):
    for _ in range(height):
        print("#")


# Function to print a row of hashes
def print_row(width):
    for _ in range(width):
        print("#", end = " ")


# Function to print a square of hashes
def print_square(row, column):
    for _ in range(row):
        print_row(column)
        print() 


# Function to get a positive integer input from the user
def get_inp(prompt):
    while True:
        n = int(input(prompt))
        if n > 0:
            break
    return n


main()