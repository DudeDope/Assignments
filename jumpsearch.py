def jump_search(arr,x):
    n = len(arr)
    jump = int(n**(1/2))
    start=0
    end=jump
    while arr[end]<x:
        start=jump
        end+=jump
    for i in range(start,end+1):
        if arr[i]==x:
            return i
    return -1
arr= [1,2,444,3,8,33,3,4,5,6,7,9,10]
result = jump_search(arr,8)
if result ==(-1):
    print('Not present')
else:
    print('index=',result)
