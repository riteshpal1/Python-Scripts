score = int(input('your score -> '))
if score>=90:
  grade = 'A'
elif score>=80:
  grade = 'B'
elif score>=60:
  grade = 'C' 
elif score >= 50:
  grade = 'D' 
else:
  grade = 'F' 
print(grade)