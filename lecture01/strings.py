name = input("what is your name? ")

# Strip whitespace from the input
name  = name.strip()

#title case the name
name  = name.title()

# Split the name into first and last
first, last = name.split(" ")

# Print the name in different formats
print(f"hello, {name}")


# Print the first name
print(f"hello, {first}")
