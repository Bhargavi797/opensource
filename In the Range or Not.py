T = int(input())
re = []
for i in range(T):
    x = int(input())
    if 67 <= x <= 45000:
        re.append("YES")
    else:
        re.append("NO")
print("\n".join(re))
