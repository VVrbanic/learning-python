num_tests = int(input())

for i in range(num_tests):
    _ = input()
    positions = [int(e) for e in input().strip().split()]
    steps = (max(positions) - min(positions)) * 2
    print(steps)