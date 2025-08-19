#this script calculates the grade based on the score input by the user
score  = int(input("Enter your score: " ))


if score >= 90 and score <= 100:
    print("Your grade is A")

elif score>=80 and score<90:
    print("Your grade is B")

elif score>=70 and score<80:
    print("Your grade is C")

else:
    print("Your grade is F ")