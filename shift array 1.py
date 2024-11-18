n = int(input())
arr = list(map(int, input().split()))
reverse_array = arr[1:]+arr[:1]
print(*reverse_array)
