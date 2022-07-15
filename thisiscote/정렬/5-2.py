#성적이 낮은 순서로 학생 출력하기
n = int(input())
grade = []
for i in range(n):
    student = input().split()
    grade.append((student[0],int(student[1])))

grade = sorted(grade,key=lambda student:student[1])
print(grade)
for student in grade:
    print(student[0],end= ' ')