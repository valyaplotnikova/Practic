grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = sorted(list({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}))
for i in range(len(grades)):
    grades[i] = sum(grades[i]) / len(grades[i])
avg_dict = dict(zip(students, grades))

print(avg_dict)
