a = [10,20,30]
b = [1,2,5]
i,j = 0,0
a_b_tuple =[(val,item) for val in a for item in b]
for val in a_b_tuple:
    a,b = val
    print(a*b)
print(a_b_tuple)

a,b = (20,10)
print(a)