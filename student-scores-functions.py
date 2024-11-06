def total_score(subject1, subject2, subject3):
    total = subject1 + subject2 + subject3
    return total

def average_score1(total, subject_count):
    average = total / subject_count
    return average

def average_score2(subject1, subject2, subject3):
    total = total_score(subject1, subject2, subject3)
    average = total / 3
    return average

def print_scores(total, average):
    print("The total score of the student is:", total)
    print("The average score of the student is:", average)


# Scores for the first student
score1_subject1 = 85
score1_subject2 = 90
score1_subject3 = 78

# Calculations for the first student
total = total_score(score1_subject1, score1_subject2, score1_subject3)
average = average_score1(total, 3)

# Output for the first student
print_scores(total, average)

# Scores for the second student
score2_subject1 = 88
score2_subject2 = 76
score2_subject3 = 92

# Calculations for the second student
total = total_score(score2_subject1, score2_subject2, score2_subject3)
average = average_score1(total, 3)

# Output for the second student
print_scores(total, average)

# Scores for the third student
score3_subject1 = 91
score3_subject2 = 85
score3_subject3 = 89

# Calculations for the third student
total = total_score(score3_subject1, score3_subject2, score3_subject3)
average = average_score1(total, 3)

# Output for the third student
print_scores(total, average)
