print("please fill free to update this file")

print("Hello moustafa")
print("Check Number if Even or odd")

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

students = ["Alice", "Bob", "Charlie", "David"]
num_students = len(students)
print(f"Number of students: {num_students}")
num_students = int(input("Enter the number of students: "))
print(f"Total students: {num_students}")
students = {
    "101": "Alice",
    "102": "Bob",
    "103": "Charlie",
    "104": "David"
}
print(f"Number of students: {len(students)}")


# Program to display calendar of the given month and year

# importing calendar module
import calendar

yy = 2014  # year
mm = 11    # month

# To take month and year input from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))
