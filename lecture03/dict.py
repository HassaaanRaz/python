#dictionary for hogwarts students

students = {
    "hermione": "Gryffindor",
    "harry": "Gryffindor",
    "ron": "Gryffindor",
    "draco": "Slytherin"
    }

# Accessing elements in a dictionary
# we will use keys as indexes while in lists indexes are numbers

print(students["hermione"])  # Gryffindor
print(students["harry"])     # Gryffindor        
print(students["ron"])       # Gryffindor
print(students["draco"])     # Slytherin

print("\n")
#we can use loop to iterate over the dictionary
for student in students: 
    print(f"{student} lives in {students[student]}")

print("\n")
for key in students: 
    print(f"{key} lives in {students[key]}")

#list of dictionaries
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"}, 
    {"name": "Draco", "house": "Slytherin", "patronus": "None"} #draco's patronus is not none, no patronus
]

# a list contain multiple dictionaries
# we can access elements in a dictionary using keys

for student in students:
    print(student["name"])

print("\n")

for student in students:
    print(student["house"])

print("\n")

for student in students:
    print(student["patronus"])

#can print all information in a dictionary
for student in students:
    print(f"The student name: {student["name"]}, lives in: {student["house"]}, as a patronus: {student["patronus"]}")