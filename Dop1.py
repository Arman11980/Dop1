grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
student = {'Jonny', 'Bilbo', 'Steve','Khendrik', 'Aaron'}
grades1 = (sum(grades[0])/5, sum(grades[1]) / 4, sum(grades[2]) / 4, sum(grades[3])/3, sum(grades[4])/5)
student_dict = dict(zip(student, grades1))

print(student_dict)