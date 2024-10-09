# Get user input as int
# Param - prompt - string
# Return - int - user input value
def get_int_input(prompt):
    # Looping until valid input
    while True:
        try:
            # user input value
            # type: int
            # Range: no specified range (-infinity to +infinity)
            value = int(input(prompt))
            return value
        # not an integer
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Start of range
# type: int
# Range: no specified range (-infinity to +infinity)
start = get_int_input("Enter the starting number: ")

# End of range
# type: int
# Range: no specified range (-infinity to +infinity)
end = get_int_input("Enter the ending number: ")

# Change step direction based on whether
# start is less than or greater than end
# type: int
# range: 1 or -1
step = 1 if start <= end else -1

# Loop from start to end (inclusive)
for number in range(start, end + step, step):
    # value is even
    if number % 2 == 0:
        print(f"{number} is even")
    # value is odd
    else:
        print(f"{number} is odd")
