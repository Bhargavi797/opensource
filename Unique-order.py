n =int(input())
arr = list(map(int, input().split()))
final_array =list(dict.fromkeys(arr))
print(*final_array)
