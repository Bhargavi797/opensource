n, m = map(int, input().split())
arr = list(map(int, input().split()))
num1 = sum(i for i in arr if i%m != 0)
num2 = sum(i for i in arr if i%m == 0)
print(-(num1-num2))
        
