from mpmath import zetazero 


def f(n):
    return 0. if n<=0 else float(zetazero(n).imag)


def find(f,y,a,b) -> int:
    return i_find(f,y,a,b)

def i_find(f,y,left,right):
    mid=(right+left)//2
    z=f(mid)
   
    if(z==y):
        return mid
    
    if(left==right):
        return -1
    
    if(y>z):
        mid=mid+1
        return i_find(f,y,mid,right)
    else:
        mid=mid-1
        return i_find(f,y,left,mid)



if __name__ == "__main__":
   
   y = f(123456789) # value in the range
   z = y + 1e-8 # value not in the range   

   #result=find(f,y,0,10000000000)
   result2=find(f,z,0,10000000000)
   print(f"RESULT 1: {result2}")
