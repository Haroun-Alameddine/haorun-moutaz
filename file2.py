print("Check Number if Even or odd")

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))


# Program to display calendar of the given month and year

# importing calendar module
import calendar

yy = int(input("Enter a Year: "))  # year
mm = int(input("Enter a Month: "))    # month

# To take month and year input from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))