'''def poisonousPlants(p):
    if hasattr(poisonousPlants, "count"):
        poisonousPlants.count += 1
    else:
        poisonousPlants.count = 1
    stack = []
    i = 0
    while i < len(p) - 1:
        if p[i] < p[i + 1]:
            stack.append(p[i])
        i = i + 1
    p = stack
    if len(p) != len(stack):
        poisonousPlants(p)
    else:
        return poisonousPlants.count + 1'''

p = [6,5,8,4,7,10,9]

p_tuple = [(p[val],p[val+1]) for val in range(0,len(p)-1)]

for val in p_tuple:
    i,j = val
    if i > j:

print(p_tuple)