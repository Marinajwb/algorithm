def count_cycle_collections(N, pieces):
 
    deg = [0] * 10
    

    for piece in pieces:
        a, b = int(piece[0]), int(piece[1])
        deg[a] += 1
        deg[b] += 1

  
    dp = [0] * 10
    dp[0] = 1
    for i in range(2, 10, 2):
        dp[i] = (i - 1) * dp[i - 2]

  
    ans = 1
    for i in range(10):
        ans *= dp[deg[i]]

    return ans


N = int(input())
pieces = [input().strip() for _ in range(N)]

result = count_cycle_collections(N, pieces)
print(result)