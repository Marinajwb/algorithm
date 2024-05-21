def gugu(num):
    for i in range(1, 10):
        a = num * i
        print(f"{num} * {i} = {a}")

num = int(input())
gugu(num)