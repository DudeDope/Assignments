

n=int(input('Enter a num:'))
n2=n**2
lgth = len(str(n2))
if lgth%2==0:
    k=int(lgth/2)
else:
    k=int((lgth-1)/2)
print(k)
strn = str(n2)
new1= strn[:k]
new2= strn[k:]
print(new1,new2)
z= int(new1) + int(new2)
if n==z:
    print(n,'is a karpekar No.')
else:
    print(n,'isnt a karpekar no.')



