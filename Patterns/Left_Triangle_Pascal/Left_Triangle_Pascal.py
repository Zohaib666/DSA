def Left_Triangle_Pascal(n):
    m=(n*2)//2
    for i in range(0,n):
        for j in range(0,m):
            print(" ",end=" ")
        m=m-1
        for k in range(0,i):
            print("*",end=" ")   
        print()    
    for i in range(0,n):
        for j in range(0,m):
            print(" ",end=" ")
        m=m+1
        for k in range(0,n-i):
            print("*",end=" ")   
        print()
Left_Triangle_Pascal(7)        