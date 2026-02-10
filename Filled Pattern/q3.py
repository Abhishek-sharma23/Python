n = int(input("Enter Number - "))       #Using 1 loop.
for i in range(1,n+1):
    print("  "*(n-i)+"* "*i)



n = int(input("Enter Number - "))       #Using 2 loops.
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")    
    print()
