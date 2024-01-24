year = int(input("Enter the year: "))

# Divisible by 4 & !100
# OR
# Divisible by 400


print(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
