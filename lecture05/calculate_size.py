def main():
    # Test case 1: file size = 1 → Expected rounded block size = 4096
    print(calculate(1))     

    # Test case 2: file size = 4096 (exactly one block) → Expected = 4096
    print(calculate(4096))  

    # Test case 3: file size = 4097 (slightly more than 1 block) → Expected = 8192
    print(calculate(4097))  

    # Test case 4: file size = 6000 → Expected rounded block size = 8192
    print(calculate(6000))  



def calculate(file_size):
    # Define block size (like filesystem block size) = 4096 bytes
    block_size = 4096

    # Number of completely filled blocks
    full_block = file_size // block_size   # integer division

    # Remaining bytes after filling complete blocks
    partial_block = file_size % block_size  

    # If there are leftover bytes, add 1 extra block
    if partial_block > 0:
        return (full_block + 1) * block_size

    # If no leftover bytes, return full blocks × block size
    return full_block * block_size   # (⚠️ correction: should be block_size, not file_size)



# Run the program
main()
