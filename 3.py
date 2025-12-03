marks = [] 
for i in range(5): 
    mark = float(input(f"Enter marks for subject {i+1}: ")) 
    marks.append(mark) 
 
total = sum(marks) 
percentage = total / 5 
print("Total Marks Obtained:", total) 
print("Percentage of Marks:", percentage) 
 
if percentage >= 90: 
    grade = 'A' 
elif percentage >= 80: 
    grade = 'B' 
elif percentage >= 70: 
    grade = 'C' 
elif percentage >= 60: 
    grade = 'D' 
else: 
    grade = 'F' 
print("Grade:", grade)
