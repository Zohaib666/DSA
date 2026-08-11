print("Butter Fly Pattern") 
r=int(input("Enter the number "))
def Butter_Fly_Pattern(r):
    for i in range(1,r):
        print("*"*i,end="")
        print(" "*(r-i)*2,end="")
        print("*"*i)
    for i in range(r,0,-1):
        print("*"*i,end="")
        print(" "*(r-i)*2,end="")
        print("*"*i)  
Butter_Fly_Pattern(r)          