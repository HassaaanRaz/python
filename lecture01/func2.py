# This file is part of the Python project.
def main():
    x = get_name("Enter your name: ")
    print(hello(x))

#hello function
# This function takes a name and returns a greeting
def hello(name = "World"):
    """Print a greeting to the user."""
    return f"Hello, {name}!"

#get_name function
# This function prompts the user for their name and returns it
def get_name(prompt):
    """Get the user's name with a prompt."""
    return input(prompt).strip()


# This is the entry point of the script
if __name__ == "__main__":
    main()