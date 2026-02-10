n=int(input("Enter Number - "))         #Using 2 lopps.
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()



n = int(input("Enter Number - "))       #Using 1 loop.
for i in range(1, n + 1):
    print("* " * i)
