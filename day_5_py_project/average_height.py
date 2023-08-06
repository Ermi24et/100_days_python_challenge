
student_heights = [155, 180 , 154, 127, 138]
sum_of_nums = 0
z = 0
for k in student_heights:
    z += 1
for i in student_heights:
    sum_of_nums += i
average = sum_of_nums / z
rounded_num = round(average)
print(f"the average height in the class is: {rounded_num}")
