# Function to check if date is valid
# @param (int) (year)
# @param (int) (month)
# @param (int) (day)
# @return (bool) (if date is valid)
def is_valid_date(year, month, day):
    # Check if year, month, and day are within valid ranges
    if year < 1 or month < 1 or month > 12 or day < 1:
        return False

    # Check days in each month
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return day <= 31
    elif month in [4, 6, 9, 11]:
        return day <= 30
    elif month == 2:
        # February (non-leap year)
        return day <= 28

    # Invalid month
    # Code never reaches this point
    return False

# Get user input
try:
    # user input of year - int
    year = int(input("Enter the year: "))
    # user input of month as number (1-12) - int
    month = int(input("Enter the month (1-12): "))
    day = int(input("Enter the day: "))
except ValueError:
    print("Invalid input. Please enter valid integers for year, month, and day.")
    exit(1)

# Check if the date is valid
if is_valid_date(year, month, day):
    print(f"{year}-{month:02d}-{day:02d} is a valid date.")
else:
    print(f"{year}-{month:02d}-{day:02d} is not a valid date.")
