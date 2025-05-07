credit_course = []
grade = []
grade_dic = {'A+': float(4.5), 'A0': float(4.0),'B+': float(3.5),'B0': float(3.0),
             'C+': float(2.5),'C0': float(2.0), 'D+': float(1.5), 'D0': float(1.0), 
             'F': float(0.0)}
for _ in range(20):
  data = input().split()
  if data[2] == 'P':
    pass
  else:
    credit_course.append(float(data[1]))
    grade.append(grade_dic[data[2]])
GPA = [credit_course[i]*grade[i] for i in range(len(grade))]
print(sum(GPA)/sum(credit_course))