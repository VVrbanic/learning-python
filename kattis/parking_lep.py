num_tests = int(input())
results = []

for i in range (0, num_tests):
    num_stores = int(input())
    positions = []
    steps = 0
    positions = sorted([int(e) for e in input().strip().split()])   
    
    for j in range(0,len(positions)-1):
        steps += positions[j+1] - positions[j]
    steps += positions[-1] - positions[0] 
        
    results.append(steps)

print(*results, sep="\n")
    