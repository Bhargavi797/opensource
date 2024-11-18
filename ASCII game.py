s= input()
r = ""
for char in s:
    if ord(char) >= 65 and ord(char)<=90:
        r += chr(ord(char)+32)
    if ord(char)>=97 and ord(char) <= 122:
        r += chr(ord(char)-32)
print(r)
