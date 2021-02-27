import sys 
# For getting input from input.txt file 
sys.stdin = open('f.txt', 'r')  
# Printing the Output to output.txt file 
sys.stdout = open('outputf', 'w') 

D,I,S,V,F = map(int, input().split())

Dir = {}
for i in range(S):
    a,b,c,d = input().strip().split()
    Dir[c]= [int(a),int(b),int(d)]
A = []
Car = {}
for i in range(V):
    A = list(input().strip().split())
    tm = 0
    for i in A[2:]:
        tm += Dir[i][2]
    tm += len(A[2:])
    if tm <= D:
        if tm in Car:
            Car[tm].append(A[1:])
        else:
            Car[tm] = [A[1:]]

# print(Car)
Car = dict(sorted(Car.items()))
Ans = {}

# A = []
# B = []
# C = []
# print(Car)
tm = 0
for t in Car:
    for i in Car[t]:
        if tm < D:
            for j in i:
                # A.append(Dir[j][1])
                # B.append(1)
                # C.append([j,Dir[j][2]])
                tm += 1
                if Dir[j][1] in Ans:
                    Ans[Dir[j][1]].append([j,1])
                else:
                    Ans[Dir[j][1]] = [[j,1]]
        else:
            break

# print(len(A))
# for i in range(len(A)):
#     print(A[i])
#     print(B[i])
#     print(*C[i])

B = []
# print(Ans)
print(len(Ans))
for i in Ans:
    print(i)
    B =[]
    for j in Ans[i]:
        if j not in B:
            B.append(j)

    print(len(B))
    # print(Ans[i])
    for j in B:
        print(*j)
