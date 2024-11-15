n = int(input())
arr = list(map(int, input().split()))
whole = sum(arr)
balanced_array = []
left = 0
for i in range(n):
    right = whole - left - arr[i]
    balanced_array.append(abs(left-right))
    left += arr[i]
print(*balanced_array)
