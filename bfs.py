bt={1:[2,3],2:[4,5,8,9],4:[6],6:[11],5:[],3:[],8:[],9:[],11:[]}
visited=[]
queue=[]

def bfs(bt,visited,queue,vertex):
    if vertex not in visited:
        queue.insert(0,vertex)
        visited.append(vertex)
    while queue:
        for adjacent in bt[queue.pop(0)]:
            if adjacent not in visited:
                visited.append(adjacent)
                queue.append(adjacent)

bfs(bt,visited,queue,1)
print(visited)