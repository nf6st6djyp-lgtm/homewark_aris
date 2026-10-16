if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

run_up=float("-inf")
run_max=float("-inf")
for run in arr:
    if run > run_max:
        run_up=run_max
        run_max = run  
    elif run_up < run < run_max:
        run_up=run
print(run_up)