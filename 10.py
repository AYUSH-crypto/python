class NegativeNumberError(Exception): 
    pass 
 
try: 
    num = int(input("Enter a positive number: ")) 
    if num < 0: 
        raise NegativeNumberError("Negative number entered!") 
except ValueError: 
    print("Invalid input; please enter an integer.") 
except NegativeNumberError as ne: 
    print(ne) 
else: 
    print("You entered:", num) 
