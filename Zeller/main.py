def zeller_congruence(day, month, year):
    if month < 3:
        month += 12
        year -= 1
    k = year % 100
    c = year // 100
    f = (day + (13*(month + 1))//5 + k + (k//4) + (c//4) - 2*c) % 7
    return f

# Get input from the user
day = int(input("Enter day (1-31): "))
month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))

# Calculate the day of the week
day_of_week = zeller_congruence(day, month, year)

# Determine the day's name
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
day_name = days_of_week[day_of_week]

print(f"The day of the week for {month}/{day}/{year} is {day_name}.")
