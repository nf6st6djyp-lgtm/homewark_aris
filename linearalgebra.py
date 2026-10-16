import numpy 

n = int(input())
matrix = [list(map(float, input().split())) for _ in range(n)]
det = numpy.linalg.det(numpy.array(matrix))
print(round(det, 2))