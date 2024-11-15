r,p = input().split()
if (r == 'S' and p == 'P') or (r=='R' and p == 'S') or (r=='P' and p == 'R'):
    print("Vignesh")
elif (r == 'R' and p == 'P') or (r=='S' and p=='R') or (r=='P' and p=='S'):
    print("Charan")
else:
    print("NULL")

