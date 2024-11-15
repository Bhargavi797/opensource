n = int(input())
p = -1 if n<0 else 1
string = str(abs(n))[::-1]
re = p*int(string)
if -2**31 <= re <= 2**31-1:
    print(re)
else:
    print(0)
