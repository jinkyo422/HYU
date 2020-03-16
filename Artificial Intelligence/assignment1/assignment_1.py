k = 0
n = 0
m = 0
sx = 0
sy = 0
ex = 0
ey = 0
keyx = 0
keyy = 0
maze = []
x = [1, 0, -1, 0]
y = [0, 1, 0, -1]

def open_file(num):
    
    global k, n, m, sx, sy, ex, ey, keyx, keyy, maze

    maze = []
    
    f = open('Maze_' + str(num) + '.txt', 'r')
    info = f.readline().split(" ")
    k = int(info[0])
    n = int(info[1])
    m = int(info[2])

    lines = f.readlines()
    for line in lines:
        item = line.split()
        item2 = list(str(item[0]))
        maze.append(item2)
    
    for i in range(n):
        for j in range(m):
            maze[i][j] = int(maze[i][j])
            if maze[i][j] == 3:
                sx = i
                sy = j
            elif maze[i][j] == 4:
                ex = i
                ey = j
            elif maze[i][j] == 6:
                keyx = i
                keyy = j

def write_file(func, length, time, arr, k):

    fname = "Maze_" + str(k) + "_" + func + "_output"
    with open(fname + '.txt', 'w') as f:
        for i in arr:
            for j in i:
                f.write(str(j))
            f.write("\n")
        f.write("---\nlength=" + str(length) + "\ntime=" + str(time) + "\n")
    
def bfs():

    global k, n, m, sx, sy, ex, ey, keyx, keyy, maze

    arr = []
    index = 0
    for i in maze:
        arr.append([])
        for j in i:
            arr[index].append(j)
        index += 1

    visit = [[0]*m for _ in range(n)]
    track = [[(0, 0)]*m for _ in range(n)]
    
    queue = []
    queue.append((sx, sy))

    length = 0
    time = 0
    flag = 0
    while queue:
        nowx, nowy = queue.pop(0)

        for i in range(4):
            nextx = nowx + x[i]
            nexty = nowy + y[i]
            
            if nextx>=0 and nextx<n and nexty>=0 and nexty<m:
                if arr[nextx][nexty] == 6:
                    track[nextx][nexty] = (nowx, nowy)
                    flag = 1
                    break
                if visit[nextx][nexty] == 0 and arr[nextx][nexty] == 2:
                    time += 1
                    visit[nextx][nexty] = 1
                    track[nextx][nexty] = (nowx, nowy)
                    queue.append((nextx, nexty))
                        
        if flag == 1:
            break

    ta, tb = keyx, keyy
    arr[ta][tb] = 5
    length += 1
    
    while True:
        a, b = track[ta][tb]
        if a == sx and b == sy:
            break
        length += 1
        arr[a][b] = 5
        ta, tb = a, b
    
    visit = [[0]*m for _ in range(n)]
    track = [[(0, 0)]*m for _ in range(n)]
    
    queue = []
    queue.append((keyx, keyy))

    flag = 0

    while queue:
        nowx, nowy = queue.pop(0)

        for i in range(4):
            nextx = nowx + x[i]
            nexty = nowy + y[i]
            
            if nextx>=0 and nextx<n and nexty>=0 and nexty<m:
                if arr[nextx][nexty] == 4:
                    track[nextx][nexty] = (nowx, nowy)
                    flag = 1
                    break
                
                if visit[nextx][nexty] == 0:
                    if arr[nextx][nexty] == 5 or arr[nextx][nexty] == 2:
                        time += 1
                        visit[nextx][nexty] = 1
                        track[nextx][nexty] = (nowx, nowy)
                        queue.append((nextx, nexty))
                    
        if flag == 1:
            break

    ta, tb = ex, ey
    length += 1
    while True:
        a, b = track[ta][tb]
        if a == keyx and b == keyy:
            break
        length += 1
        arr[a][b] = 5
        ta, tb = a, b
    
    write_file("BFS", length, time, arr, k)

def ids():

    global k, n, m, sx, sy, ex, ey, keyx, keyy, maze

    arr = []
    index = 0
    for i in maze:
        arr.append([])
        for j in i:
            arr[index].append(j)
        index += 1

    depth = 0
    length = 0
    time = 0
    track = [[(0, 0)]*m for _ in range(n)]
    
    while depth < n*m:
        visit = [[0]*m for _ in range(n)]
        stack = []
        stack.append((sx, sy, 0))
        flag = 0

        while stack:
            nowx, nowy, nowdep = stack.pop()
            nextdep = nowdep + 1
           
            if nextdep <= depth:
                for i in range(4):
                    nextx = nowx + x[i]
                    nexty = nowy + y[i]

                    if nextx>=0 and nextx<n and nexty>=0 and nexty<m:
                        if arr[nextx][nexty] == 6:
                            track[nextx][nexty] = (nowx, nowy)
                            flag = 1
                            break
                        
                        if visit[nextx][nexty] == 0:
                            if arr[nextx][nexty] == 5 or arr[nextx][nexty] == 2:
                                time += 1
                                visit[nextx][nexty] = 1
                                track[nextx][nexty] = (nowx, nowy)
                                stack.append((nextx, nexty, nextdep))
                
        if flag == 1:
            break
        depth += 1 

    ta, tb = keyx, keyy
    arr[ta][tb] = 5
    length += 1
    
    while True:
        a, b = track[ta][tb]
        if a == sx and b == sy:
            break
        length += 1
        arr[a][b] = 5
        ta, tb = a, b

    depth = 0
    
    while depth < n*m:
        visit = [[0]*m for _ in range(n)]
        stack = []
        stack.append((keyx, keyy, 0))
        flag = 0

        while stack:
            nowx, nowy, nowdep = stack.pop()
            nextdep = nowdep + 1
           
            if nextdep <= depth:
                for i in range(4):
                    nextx = nowx + x[i]
                    nexty = nowy + y[i]

                    if nextx>=0 and nextx<n and nexty>=0 and nexty<m:
                        if arr[nextx][nexty] == 4:
                            track[nextx][nexty] = (nowx, nowy)
                            flag = 1
                            break
                        
                        if visit[nextx][nexty] == 0:
                            if arr[nextx][nexty] == 5 or arr[nextx][nexty] == 2:
                                time += 1
                                visit[nextx][nexty] = 1
                                track[nextx][nexty] = (nowx, nowy)
                                stack.append((nextx, nexty, nextdep))
                
        if flag == 1:
            break
        depth += 1 
    
    ta, tb = ex, ey
    length += 1
    
    while True:
        a, b = track[ta][tb]
        if a == keyx and b == keyy:
            break
        length += 1
        arr[a][b] = 5
        ta, tb = a, b

    write_file("IDS", length, time, arr, k)
    
def greedy_bfs():

    global k, n, m, sx, sy, ex, ey, keyx, keyy, maze

    arr = []
    index = 0
    for i in maze:
        arr.append([])
        for j in i:
            arr[index].append(j)
        index += 1

    visit = [[0]*m for _ in range(n)]
    track = [[(0, 0)]*m for _ in range(n)]
    
    priority_queue = []
    priority_queue.append((sx, sy, abs(sx-keyx)+abs(sx-keyy)))
    
    length = 0
    time = 0
    flag = 0
    while priority_queue:
        priority_queue = sorted(priority_queue, key=lambda priority_queue: priority_queue[2])
        nowx, nowy, nowman = priority_queue.pop(0)

        for i in range(4):
            nextx = nowx + x[i]
            nexty = nowy + y[i]
            
            if nextx>=0 and nextx<n and nexty>=0 and nexty<m:
                if arr[nextx][nexty] == 6:
                    track[nextx][nexty] = (nowx, nowy)
                    flag = 1
                    break
                if visit[nextx][nexty] == 0 and arr[nextx][nexty] == 2:
                    time += 1
                    visit[nextx][nexty] = 1
                    track[nextx][nexty] = (nowx, nowy)
                    priority_queue.append((nextx, nexty,abs(nextx-keyx)+abs(nextx-keyy)))
                        
        if flag == 1:
            break

    ta, tb = keyx, keyy
    arr[ta][tb] = 5
    length += 1
    
    while True:
        a, b = track[ta][tb]
        if a == sx and b == sy:
            break
        length += 1
        arr[a][b] = 5
        ta, tb = a, b
        
    visit = [[0]*m for _ in range(n)]
    track = [[(0, 0)]*m for _ in range(n)]
    
    priority_queue = []
    priority_queue.append((keyx, keyy, abs(keyx-ex)+abs(keyy-ey)))

    flag = 0
    while priority_queue:
        priority_queue = sorted(priority_queue, key=lambda priority_queue: priority_queue[2])
        nowx, nowy, nowman = priority_queue.pop(0)

        for i in range(4):
            nextx = nowx + x[i]
            nexty = nowy + y[i]
            
            if nextx>=0 and nextx<n and nexty>=0 and nexty<m:
                if arr[nextx][nexty] == 4:
                    track[nextx][nexty] = (nowx, nowy)
                    flag = 1
                    break
                if visit[nextx][nexty] == 0:
                    if arr[nextx][nexty] == 5 or arr[nextx][nexty] == 2:
                        time += 1
                        visit[nextx][nexty] = 1
                        track[nextx][nexty] = (nowx, nowy)
                        priority_queue.append((nextx, nexty,abs(nextx-ex)+abs(nextx-ey)))
                        
        if flag == 1:
            break

    ta, tb = ex, ey
    length += 1

    while True:
        a, b = track[ta][tb]
        if a == keyx and b == keyy:
            break
        length += 1
        arr[a][b] = 5
        ta, tb = a, b

    write_file("GBFS", length, time, arr, k)
    
def a_star():

    global k, n, m, sx, sy, ex, ey, keyx, keyy, maze

    arr = []
    index = 0
    for i in maze:
        arr.append([])
        for j in i:
            arr[index].append(j)
        index += 1

    visit = [[0]*m for _ in range(n)]
    track = [[(0, 0)]*m for _ in range(n)]
    
    priority_queue = []
    priority_queue.append((sx, sy, abs(sx-keyx)+abs(sx-keyy), 0))
    
    length = 0
    time = 0
    flag = 0
    while priority_queue:
        priority_queue = sorted(priority_queue, key=lambda priority_queue: priority_queue[2])
        nowx, nowy, nowman, nowcost = priority_queue.pop(0)
        nextcost = nowcost + 1
        
        for i in range(4):
            nextx = nowx + x[i]
            nexty = nowy + y[i]
            
            if nextx>=0 and nextx<n and nexty>=0 and nexty<m:
                if arr[nextx][nexty] == 6:
                    track[nextx][nexty] = (nowx, nowy)
                    flag = 1
                    break
                if visit[nextx][nexty] == 0 and arr[nextx][nexty] == 2:
                    time += 1
                    visit[nextx][nexty] = 1
                    track[nextx][nexty] = (nowx, nowy)
                    priority_queue.append((nextx, nexty, nextcost+abs(nextx-keyx)+abs(nextx-keyy), nextcost))
                        
        if flag == 1:
            break

    ta, tb = keyx, keyy
    arr[ta][tb] = 5
    length += 1
    
    while True:
        a, b = track[ta][tb]
        if a == sx and b == sy:
            break
        length += 1
        arr[a][b] = 5
        ta, tb = a, b
        
    visit = [[0]*m for _ in range(n)]
    track = [[(0, 0)]*m for _ in range(n)]
    
    priority_queue = []
    priority_queue.append((keyx, keyy, abs(keyx-ex)+abs(keyy-ey), 0))

    flag = 0
    while priority_queue:
        priority_queue = sorted(priority_queue, key=lambda priority_queue: priority_queue[2])
        nowx, nowy, nowman, nowcost = priority_queue.pop(0)
        nextcost = nowcost + 1
        
        for i in range(4):
            nextx = nowx + x[i]
            nexty = nowy + y[i]
            
            if nextx>=0 and nextx<n and nexty>=0 and nexty<m:
                if arr[nextx][nexty] == 4:
                    track[nextx][nexty] = (nowx, nowy)
                    flag = 1
                    break
                if visit[nextx][nexty] == 0:
                    if arr[nextx][nexty] == 5 or arr[nextx][nexty] == 2:
                        time += 1
                        visit[nextx][nexty] = 1
                        track[nextx][nexty] = (nowx, nowy)
                        priority_queue.append((nextx, nexty, nextcost+abs(nextx-ex)+abs(nextx-ey), nextcost))
                        
        if flag == 1:
            break

    ta, tb = ex, ey
    length += 1

    while True:
        a, b = track[ta][tb]
        if a == keyx and b == keyy:
            break
        length += 1
        arr[a][b] = 5
        ta, tb = a, b

    write_file("A_star", length, time, arr, k)
    
def main():

    for i in range(1, 4):
        open_file(i)
        
        bfs()
        ids()
        greedy_bfs()
        a_star()
    
if __name__ == "__main__":
    main()
