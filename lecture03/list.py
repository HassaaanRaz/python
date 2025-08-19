#we'll be working with lists in this file

students = ["Hermione", "Harry", "Ron"]

# Accessing elements in a list
print(students[0])  # Hermione
print(students[1])  # Harry
print(students[2])  # Ron

#using for loop tto iterate over the list
for student in students:
    print(f"{student} is a student")

#using rnge to iterate over the list
for i in range(len(students)):
    print(f"{i+1}. {students[i]} is a student")
    

#house list
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]