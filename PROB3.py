
v= 'AEIOUaeiou'
str=input('Enter string:')
l=[]
for i in str:
    if i in v:
        l.append(i)
if len(l)==0 or len(l)==1 or len(l)==2:
    dummy=True
else:
    c= str.index(l[1])-str.index(l[0])
    for j in range(1,len(l)):
        if str.index(l[j])-str.index(l[j-1])==c:
            dummy=True
        else:
            dummy=False
            break
if dummy==True:
    print('Given string is NICE')
if dummy==False:
    print('Given string is NOT NICE')



