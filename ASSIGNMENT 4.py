TASK 1

try:
    with open("sample.txt", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")



TASK 2

data = input("Enter a value: ")

with open("output.txt", "w") as file:
    file.write(data + "\n")

with open("output.txt", "a") as file:
    file.write("Appended data\n")


with open("output.txt", "r") as file:
    print(file.read())
