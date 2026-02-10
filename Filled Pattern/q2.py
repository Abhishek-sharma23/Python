n=int(input("Enter Number - "))     #Using 1 loop.
for i in range(n, 0, -1):
    print("* " * i)



n = int(input("Enter Number - "))       #Using 2 loops.
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
