def countLowerLetters(list1):
    count = 0
    
    for word in list1:
        for char in word:
            if char.islower():
                count += 1


    return count



list1 = ["Hello", "world", "I", "am", "an", "AI", "assistant"]
count = countLowerLetters(list1)

print(f"Total number of lowercase letters: {count}")
