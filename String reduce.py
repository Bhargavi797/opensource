s1 = input()
re = ""
c=1
for i in range(1, len(s1)):
    if s1[i] == s1[i-1]:
        c += 1
    else:
        re += s1[i-1] + str(c)
        c =1
if s1:
    re += s1[-1] + str(c)
print(re)
