n=int(input("Enter Number - "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==n or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()