n=int(input())

i=1

while(i<=n):
    k=i-1
    while(k<n):
        print(" ",end='')
        k+=1

    j=1
    while(j<=i):
        print("* ",end='')
        j=j+1

    print()
    i+=1
