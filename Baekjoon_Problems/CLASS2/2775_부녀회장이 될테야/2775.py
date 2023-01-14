t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    List = [j for j in range(1,n+1)]
    for r in range(1,k+1):
        for a in range(1, n):
            List[a] += List[a-1]
    print(List[n-1])




