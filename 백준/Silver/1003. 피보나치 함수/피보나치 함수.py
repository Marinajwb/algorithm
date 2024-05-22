A= int(input())
for _ in range(A):
    N = int(input())
    a, b = 1, 0 
    for i in range(N):
     
        a,b = b, a+b 
    print(a,b)
