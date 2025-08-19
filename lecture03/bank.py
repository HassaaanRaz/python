# Bank Greeting Program
# Depending on how a user greets, the "bank" gives them a different response.

def main():
    # Ask the user for a greeting (e.g., Hello, Hi, Hey, etc.)
    greet = get_inp("Greeting: ")
    
    # Process the greeting and get the response
    result = check(greet)

    # Print the "bank" response ($0, $20, or $100)
    print(result)


def get_inp(prompt):
    # Take input, remove leading/trailing spaces, and convert to uppercase
    inp = input(prompt).strip().upper()

    # Ensure the input has more than 3 characters (minimum valid greeting)
    if len(inp) > 3:
        try:
            # Split the input into two parts:
            # 'a' will store the first word, 'b' will store the rest of the sentence
            a, b = inp.split(maxsplit=1)  
        except ValueError:
            # If the user only entered one word, store it in 'a'
            a = inp 

        # Remove commas (if any) from the first word
        c = a.replace(",", "")
        return c
    else:
        # If input is too short, mark it as invalid
        return "INVALID INPUT"


def check(greet):
    # If the greeting is exactly "HELLO", the bank gives $0
    if greet == "HELLO":
        return "$0"
    
    # If the greeting starts with 'H' (e.g., HI, HEY, HOWDY) but is not "HELLO"
    # the bank gives $20
    elif greet[0] == "H":
        return "$20"

    # For all other greetings (not starting with H), the bank gives $100
    else:
        return "$100"


# Start the program
main()
