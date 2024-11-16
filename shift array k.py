def array(arr, k):
    k %= len(arr)
    reverse = arr[-k:]+arr[:-k]
    return reverse
n = int(input())
arr = list(map(int, input().split()))
k = int(input())
print(*array(arr, k))
