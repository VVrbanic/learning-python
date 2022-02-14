nums = sorted([int(e) for e in input().strip().split()])

num_order = input().strip()

num_dict = {
               "A": nums[0],
               "B": nums[1],
               "C": nums[2]
}

output = []

for i in num_order:
    output.append(num_dict[i])
    
print(*output)