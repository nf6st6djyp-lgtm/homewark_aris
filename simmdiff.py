
n = int(input())
set1 = set(map(int, input().split()))

m = int(input())
set2 = set(map(int, input().split()))

sym_diff = set1.symmetric_difference(set2)

for num in sorted(sym_diff):
    print(num)

