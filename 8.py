base = int(input("Enter base: ")) 
power = int(input("Enter power: ")) 
result = 1 
i = 0 
while i < power: 
    result *= base 
    i += 1 
print(f"{base} raised to the power {power} is {result}") 
