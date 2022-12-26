def inp():
    print("Input n ")
    n = int(input())
    return(n)

def factor(n): 
    if(n==1 or n==0): 
        return 1 
    else: 
        return n*factor(n-1) 
        

n = inp()

print("The factorial of ", n," = ", factor(n))
