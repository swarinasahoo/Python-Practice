name = input("Enter student name: ")


m1 = float(input("Enter marks 1: "))
m2 = float(input("Enter marks 2: "))
m3 = float(input("Enter marks 3: "))

total = m1 + m2 + m3
average = total/3

if average>= 40:
    result = "pass"
else:
    result = "fail"
    
# print the result formatted 
print('='*30)
print('STUDENT RESULT SUMMARY')
print(f'Name : {name}')
# :.2f (For printing decimal point for 2 times)
print(f'Marks in subject 1 : {m1:.2f}')
print(f'Marks in subject 2 : {m2:.2f}')
print(f'Marks in subject 3 : {m3:.2f}')
print('='*30)
print(f'Total Marks : {total}')
print(f'Average Marks : {average:.2f}')
print(f'Result status : {result}')