def is_armstrong(num): 
    temp = num 
    sum_of_cubes = 0 
    while temp > 0: 
        digit = temp % 10 
        sum_of_cubes += digit ** 3 
        temp //= 10 
    return sum_of_cubes == num 
 
num = int(input("Enter number: ")) 
if is_armstrong(num): 
    print(num, "is Armstrong") 
else: 
    print(num, "is not Armstrong")
