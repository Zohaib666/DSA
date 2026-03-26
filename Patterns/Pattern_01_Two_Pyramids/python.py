# Two pyramids solutions using functions   
def two_pyramids(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end=" ")
        print()  
    print("\n")      
    for i in range(n):
        for j in range(n-i):
            print("*",end=" ")
        
        print()
two_pyramids(7)       
    
