n=int(input("Enter Number - "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for k in range(1,n):
        if k==n-1 or i+k==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or i+j==n+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for k in range(1,n):
        if k==n-1 or i==k+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()