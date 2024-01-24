year = int(input("Enter the year: "))

# Divisible by 4 & !100
# OR
# Divisible by 400

if year % 4 == 0 and year % 100!= 0:
	print("Leap")
elif year % 400 == 0:
	print("Leap")
else:
	print("Not leap")
