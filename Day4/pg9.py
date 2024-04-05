n=int(input())
a=n+1
i=1

while(i<=n):
    
    k=1
    while(k<i):
        print("  " ,end='')
        
        k+=1

    j=1
    a=a-1
    while(j<=a):
        print("* ",end='')
        j=j+1
       

    print()
    i+=1