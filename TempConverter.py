def celsius_to_fahrenheit(celsius):

    fahrenheit = celsius * (9/5) + 32
    
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):

    celsius = (fahrenheit - 32) * (5/9)

    return celsius


temp = float(input("What is the temperature? "))
tempType = input("Is it 'C' or 'F'? ")

if tempType == "C":
    convertedTemp = celsius_to_fahrenheit(temp)
elif tempType == "F":
    convertedTemp = fahrenheit_to_celsius(temp)
else:
    convertedTemp = "Not valid type"

print("Converted temp: " + str(convertedTemp))

