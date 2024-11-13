# Information for the first employee
name1 = "Alice"
hours_worked1 = 40
hourly_rate1 = 20

# Calculations for the first employee
if hours_worked1 > 40:
    overtime_hours1 = hours_worked1 - 40
    overtime_pay1 = overtime_hours1 * (hourly_rate1 * 1.5)
else:
    overtime_pay1 = 0

regular_pay1 = min(hours_worked1, 40) * hourly_rate1
total_pay1 = regular_pay1 + overtime_pay1

# Output for the first employee
print("The total pay for", name1, "is:", total_pay1)

# Information for the second employee
name2 = "Bob"
hours_worked2 = 45
hourly_rate2 = 22

# Calculations for the second employee
if hours_worked2 > 40:
    overtime_hours2 = hours_worked2 - 40
    overtime_pay2 = overtime_hours2 * (hourly_rate2 * 1.5)
else:
    overtime_pay2 = 0

regular_pay2 = min(hours_worked2, 40) * hourly_rate2
total_pay2 = regular_pay2 + overtime_pay2

# Output for the second employee
print("The total pay for", name2, "is:", total_pay2)

# Information for the third employee
name3 = "Charlie"
hours_worked3 = 38
hourly_rate3 = 18

# Calculations for the third employee
if hours_worked3 > 40:
    overtime_hours3 = hours_worked3 - 40
    overtime_pay3 = overtime_hours3 * (hourly_rate3 * 1.5)
else:
    overtime_pay3 = 0

regular_pay3 = min(hours_worked3, 40) * hourly_rate3
total_pay3 = regular_pay3 + overtime_pay3

# Output for the third employee
print("The total pay for", name3, "is:", total_pay3)