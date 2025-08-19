def main():

    number  = get_inp("Enter a positive number: ")
    meow(number)




def meow(n):
    for _ in range(n):
        print("meow")


def get_inp(prompt):
    while True:
        number = int(input(prompt))
        if number > 0:
            break
    return number



main()