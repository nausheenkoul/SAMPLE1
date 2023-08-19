def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

def Pewdipe(year, month, day):
    # Determine if the year is a leap year
    leap_year = is_leap_year(year)

    # Adjust the day of the month for February
    if month == 2:
        if leap_year:
            day += 1

    # Determine the century
    if year >= 0 and year < 100:
        century = year // 100 + 1
    else:
        century = year // 100

    # Calculate the day of the week using the Zeller rule
    f = (day + (13*(month+1))//5 + year + year//4 + 5*century//4 - 2*century) % 7

    # Return the day of the week as a string
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return days_of_week[f]

# Prompt the user for a date
date_input = input("Enter the date in the format 'YYYY MM DD': ")
try:
    year, month, day = map(int, date_input.split())
    if month < 1 or month > 12 or day < 1 or day > 31:
        raise ValueError("Invalid month or day")
except ValueError:
    print("Invalid date format.")
else:
    # Find the day of the week
    day_of_week = Pewdipe(year, month, day)
    leap_status = "leap" if is_leap_year(year) else "not leap"

    # Print the result
    print("The day of the week for", month, "/", day, "/", year, "is", day_of_week)
    print("The year", year, "is", leap_status)
