
def special_num(n): 
    s=0 
    k=1 
    for i in str(n): 
        s+=int(i) 
        k*=int(i) 
    new_n= s+k 
    if new_n==n: 
        return True 
    else: 
        return False 
t=int(input()) 
for y in range(10**(t-1),10**t): 
    if special_num(y)==True: 
        k=y 
        break 
    else: 
            k='Not found'
print(k)