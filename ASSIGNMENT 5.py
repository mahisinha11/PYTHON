TASK 1


student_marks = {
    "Amit": 85,
    "Riya": 92,
    "Kunal": 78,
    "Sneha": 88
}


name = input("Enter the student's name: ")


if name in student_marks:
    print(f"Marks of {name}: {student_marks[name]}")
else:
    print("Student name not found.")


TASK 2



numbers = list(range(1, 11))

first_five = numbers[:5]

reversed_list = first_five[::-1]

print("Extracted list:", first_five)
print("Reversed list:", reversed_list)

