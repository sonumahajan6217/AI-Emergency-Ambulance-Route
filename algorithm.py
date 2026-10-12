import heapq

def heuristic(node, goal):
    return abs(node[0]-goal[0]) + abs(node[1]-goal[1])

def neighbors(node, grid):
    r,c=node
    for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr,nc=r+dr,c+dc
        if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]==0:
            yield (nr,nc)

def reconstruct(came_from, current):
    path=[current]
    while current in came_from:
        current=came_from[current]; path.append(current)
    return path[::-1]

def a_star(grid, start, goal):
    heap=[]; counter=0
    g={start:0}; came={}; closed=set(); explored=0
    heapq.heappush(heap,(heuristic(start,goal),0,counter,start))
    while heap:
        _, current_g, _, current=heapq.heappop(heap)
        if current in closed: continue
        closed.add(current); explored+=1
        if current==goal: return reconstruct(came,current), explored
        for nxt in neighbors(current,grid):
            if nxt in closed: continue
            tentative=current_g+1
            if tentative < g.get(nxt,float('inf')):
                g[nxt]=tentative; came[nxt]=current; counter+=1
                heapq.heappush(heap,(tentative+heuristic(nxt,goal),tentative,counter,nxt))
    return [], explored
