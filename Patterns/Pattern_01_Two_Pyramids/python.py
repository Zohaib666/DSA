'''n=5
for i in range(n):
    for j in range(n-i-1):
        print("*",end="")
    for k in range (i+1):
        print("3",end="")
    print()'''
"""#first solution for pyramid pattern 
n=7
m=(n*2)-2
for i in range(0,7):

    for j in range(0,m):
        print(end=" ")
    m=m-1  
    for j in range(0,i+1):
        print("*",end=" ")  
    print("    ")
#second solution for pyramid pattern 
def full_pyramid(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print("",end=" ")
        for k in range(1,2*i):
            print("*", end="")
        print()        
full_pyramid(7)
#Third solution for pyramid pattern
rows = int(input("Enter number of rows: "))

k = 0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
   
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
   
    k = 0
    print()"""      
# Check seo ai tools which help to improve seo 







'''n=int(input("Enter the number between 10 "))
for i in range(n):
    for j in range(n):
        if(i==0 or i==n-1 or j==0 or j==n-1):
            print("*",end=" ")
        else:
            print(".",end=" ")
    print()'''  

'''#n=int(input("Enter the number between 10 "))
n=6

for i in range(5,0,-1):
    for j in range(i):
            print("*",end=" ")
       
    print()'''




    #for j in range(0,n):
        #if(i==0 or i==n-1 or j==0 or j==n-1):
            #print("*",end=" ")
        #else:
            #print(".",end=" ")
    #print()   
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
    
