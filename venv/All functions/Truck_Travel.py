petrol_pumps = [[1,5],[10,3],[3,4]]

N=input()

sumi=0;

maxi=0;

j=0;

for i in range(N):

    a,b=raw_input().split()

    sumi+=int(a)-int(b)

    if(sumi<0):

        sumi=0

        j=i+1
print(j)

