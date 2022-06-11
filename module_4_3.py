graph={
    1: [1, 3],
    2: [2, 4, 8],
    3: [5, 6, 8],
    4: [3, 7, 9],
    5: [6, 7],
    6: [5],
    7: [4, 5, 8],
    8: [1, 2, 3, 7],
    9: [5],
}
visited=set() #Посещена ли вершина?
q=[] #Очередь
BFS=[]

def width_search(v):
	if v in visited:
		return
	visited.add(v)
	BFS.append(v)
	for i in graph[v]:
		if not i in visited:
			q.append(i)
	while q:
		width_search(q.pop(0))

start=1
width_search(start)
print (BFS)

