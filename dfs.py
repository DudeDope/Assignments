bt={1:[2,3],2:[4,5],4:[6],6:[],5:[],3:[]}
visited=[]
def dfs(bt,visited,vertex):
    if vertex not in visited:
        visited.append(vertex)
    print(vertex)
    for adjacent in bt[vertex]:
        dfs(bt,visited,adjacent)
dfs(bt,visited,1)
print(visited)
