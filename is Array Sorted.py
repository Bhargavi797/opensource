n = int(input())
arr = list(map(int, input().split()))
re = all(arr[i] <= arr[i+1] for i in range(n-1))
print(str(re).lower())
