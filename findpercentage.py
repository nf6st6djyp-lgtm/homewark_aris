if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

media=0
for name in student_marks: 
    if name==query_name:
        tot=0
        for score in student_marks[name]:
            tot += score
        media = tot/(len(student_marks[name]))
        
print(f"{media:.2f}")
