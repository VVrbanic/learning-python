num_tests = int(input())
results = []

for i in range (0, num_tests):
    num_stores = int(input())
    positions = []
    steps = 0
    #positions = sorted(list(map(int, input().strip().split()))[:num_stores])
    positions = sorted([int(e) for e in input().strip().split()])   
    
    if len(positions) == 1:
        results.append(0)
    else:
        for j in range (0,len(positions)-1):
            steps = steps + (abs(positions[j]-positions[j+1]))
        steps = steps + (abs(positions[0]-positions[-1]))
        
    if steps > 0:
        results.append(steps)

print(*results, sep="\n")
    