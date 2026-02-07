n=int(input("Enter Number - "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or i==j or i==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for k in range(1,n+1):
        if i==n or k==n or i+k==n+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()