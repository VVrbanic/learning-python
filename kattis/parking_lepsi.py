num_tests = int(input())
results = []

for i in range (0, num_tests):
    num_stores = int(input())
    positions = []
    steps = 0
    positions = sorted([int(e) for e in input().strip().split()])   
    
    steps = (positions[-1] - positions[0]) * 2
        
    results.append(steps)

print(*results, sep="\n")
    