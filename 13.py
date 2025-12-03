s = input("Enter a string: ").lower() 
vowels = "aeiou" 
vowel_count = consonant_count = digit_count = 0 
for char in s: 
    if char in vowels: 
        vowel_count += 1 
    elif char.isalpha(): 
        consonant_count += 1 
    elif char.isdigit(): 
        digit_count += 1 
print("Vowels:", vowel_count) 
print("Consonants:", consonant_count) 
print("Digits:", digit_count) 
print("Length of string:", len(s))
