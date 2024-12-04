def calculations(nums):
    total = 0
    product = 1
    
    for n in nums:
        if n > 0:
            total += n
        else:
            product *= n

    return total, product


nums = []

number = int(input("Enter a number: "))

while number != 0:
    nums.append(number)
    number = int(input("Enter a number: "))


total, product = calculations(nums)

print(f"Sum of positives: {total}")
print(f"Product of negatives: {product}")
