n = int(input())
columns = input().split()

# Find index of the 'MARKS' column
marks_index = columns.index('MARKS')

total_marks = 0

for _ in range(n):
    data = input().split()
    total_marks += int(data[marks_index])

average = total_marks / n
print(f"{average:.2f}")
