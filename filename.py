filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print("File not found.")
    exit()

num_lines = len(lines)
print(f"The file contains {num_lines} lines.")

while True:
    try:
        line_number = int(input(f"Enter a line number (1-{num_lines}, or 0 to quit): "))
        if line_number == 0:
            print("Exiting program.")
            break
        elif 1 <= line_number <= num_lines:
            print(lines[line_number - 1].strip())
        else:
            print(f"Invalid line number. Please enter a number between 1 and {num_lines}, or 0 to quit.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")