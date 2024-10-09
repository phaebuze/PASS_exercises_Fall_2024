# Checks to see if sidelength values
# are capable to create a triangle.
# Parameters - a, b, c
#           - integer
#           - range: > 0 (1+)
#           - values might be different
# Return    - boolean
#           - valid triangle
def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

# Finds the type of trangle,
# based on comparing sidelengths.
# Parameters - a, b, c
#           - integer
#           - range: > 0 (1+)
#           - values might be different
# Return    - string
#           - triangle type
def triangle_type(a, b, c):
    # equaliateral triangle - all sides equal
    if a == b == c:
        return "Equilateral"
    # isosceles triangle - 2 sides equal
    elif a == b or b == c or a == c:
        return "Isosceles"
    # scalene triangle - no sides equal
    else:
        return "Scalene"

# Get input from user
# Check if valid input, based on range + data type
# Parameter - prompt
#           - string
#           - expect: "Enter a length: "
# Return    - value
#           - integer
#           - user input side length
def get_side_length(prompt):
    # Loop until valid value input
    while True:
        try:
            # user input side length
            # integer, range: > 0 (1+)
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Side length must be a positive integer.")
        # not an integer        
        except ValueError:
            print("Invalid input. Please enter an integer.")


print("Enter the lengths of the three sides of the triangle:")
# input of side length 1
# integer, range: > 0
side1 = get_side_length("Side 1: ")

# input of side length 2
# integer, range: > 0
side2 = get_side_length("Side 2: ")

# input of side length 3
# integer, range: > 0
side3 = get_side_length("Side 3: ")

# check if valid triangle
if is_valid_triangle(side1, side2, side3):
    print(f"The triangle is {triangle_type(side1, side2, side3)}.")
else:
    print("The given side lengths do not form a valid triangle.")
