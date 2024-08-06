grid = [[9,1,7],[8,9,2],[3,4,6]]
repeated = 0
missing = 0

example = [num + 1 for num in range(len(grid) ** 2)]
sequence = []

for i in grid:
    for j in i:
        sequence.append(j)


for num in example:
    if num not in sequence:
        missing = num
    elif sequence.count(num) == 2:
        repeated = num


answer = []
answer.append(repeated)
answer.append(missing)

print(answer)
