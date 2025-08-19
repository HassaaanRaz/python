def main():
    # Get the user greeting after cleaning/validating input
    greeting = get_input("Greeting: ")
    
    # If the input was invalid, just print the error
    if greeting == "INVALID INPUT":
        print(greeting)
    else:
        # Otherwise, check the greeting and get bank's response
        result = check_greeting(greeting)
        print(result)


def get_input(prompt):
    # Ask the user for input and remove leading/trailing spaces
    user_input = input(prompt).strip()

    # If user entered nothing, return INVALID
    if len(user_input) == 0:
        return "INVALID INPUT"
    
    # Convert to uppercase and replace commas with spaces
    # Example: "Hello, world" → "HELLO WORLD"
    cleaned_input = user_input.replace(",", " ").upper()

    # Take only the first word from the greeting
    # Example: "HELLO WORLD" → "HELLO"
    cleaned_input_a = cleaned_input.split(maxsplit=1)[0]  

    return cleaned_input_a


def check_greeting(greet):
    # Double-check: if somehow an empty string slipped through
    if greet == "":
        return "INVALID INPUT"

    # Rule 1: Exact word "HELLO" → bank gives $0
    if greet == "HELLO":
        return "$0"
    
    # Rule 2: Any greeting starting with 'H' (HI, HEY, HOWDY) → bank gives $20
    elif greet.startswith("H"):
        return "$20"
    
    # Rule 3: Anything else (GOOD MORNING, BYE, etc.) → bank gives $100
    else:
        return "$100"


# Program entry point
if __name__ == "__main__":
    main()
