if __name__ == '__main__':
    names=[]
    scores=[]
    for _ in range(int(input())):
        names.append(input())
        scores.append(float(input()))

score_down=10000
score_min=10000
for i in range(len(scores)):
    if  scores[i] < score_min:
        score_down=score_min
        score_min = scores[i]  
    elif score_down > scores[i] > score_min:
        score_down= scores[i]

fnames=[]
for i in range(len(names)):
    if scores[i]==score_down:
        fnames.append(names[i])
        
fnames.sort()
for name in fnames:
    print(name)
        
        
