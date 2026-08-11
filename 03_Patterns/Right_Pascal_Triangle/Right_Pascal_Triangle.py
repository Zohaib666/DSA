def Right_Pascal_Triangle(n):
    m=(n*2)-2
    for i in range(n):
        for j in range(i):
            print("*",end=" ")     
        print() 
    for i in range(n):
        for j in range(n-i):
            print("*",end=" ")
        print()
Right_Pascal_Triangle(7)        