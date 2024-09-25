# Function to ask user for student's score
def get_user_input():
    # Try to run code
    try:
        # Get student grade, store in variable 'score'
        score = int(input("Enter the student's score (out of 100): "))

        # Check score, must be greater than, or equal to zero.
        # or less than or equal to 100
        if score < 0 or score > 100:
            # Else, go to ValueError.
            raise ValueError()

        # Retruns valid user input
        return score

    # print error message if 'ValueError'
    except ValueError:
        print("Invalid input. Please enter a positive integer between 0 and 100.")
        return get_user_input()

# Function to convert number score to letter grade
# @param (int) (score)
#       user inputted number
# @return (string) (letter grade, A-F)
def convert_to_letter_grade(score):    
    # if score is greater than, or equal to 90, letter grade is A
    if score >= 90:
        return "A"
    # if score is less than 90 AND greater than, or equal to 80, letter grade is B
    elif score >= 80:
        return "B"
    # if score is less than 80 AND greater than, or equal to 70, letter grade is C
    elif score >= 70:
        return "C"
    # if score is less than 70 AND greater than, or equal to 60, letter grade is D
    elif score >= 60:
        return "D"
    # if score is less than 60 letter grade is F
    else:
        return "F"

# Get user input
# Run get_user_input()
# student_score stores user number grade (int)
student_score = get_user_input()

# Convert to letter grade
# Run convert_to_letter_grade()
# letter_grade stores converted user grade (string)
letter_grade = convert_to_letter_grade(student_score)

print(f"The student's score of {student_score} corresponds to the letter grade: {letter_grade}")
