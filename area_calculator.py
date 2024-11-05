import math

# CREATE FUNCTIONS
# CIRCLE AREA


# RECTANGLE AREA


# TRIANGLE AREA



while True:
    print("\nArea Calculator")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Exit")
    choice = input("Choose a shape to calculate the area: ")

    # ADD FUNCTION CALLS 
    if choice == '1':
        radius = float(input("Enter the radius of the circle: "))
        print(f"The area of the circle is: ")
    elif choice == '2':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        print(f"The area of the rectangle is: ")
    elif choice == '3':
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        print(f"The area of the triangle is: ")
    elif choice == '4':
        print("Exiting the area calculator. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")