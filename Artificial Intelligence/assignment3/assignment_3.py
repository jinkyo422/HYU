import random

x = [1, 0, -1, 0]
y = [0, 1, 0, -1]

def open_file(num):
    
    maze = []
    
    f = open('FrozenLake_' + str(num) + '.txt', 'r')
    info = f.readline().split(" ")
    k = int(info[0])
    n = int(info[1])
    m = int(info[2])

    lines = f.readlines()
    for line in lines:
        item = line.split()
        item2 = list(str(item[0]))
        maze.append(item2)

    return maze, k, n, m

def write_file(solution, k, n, m):
    
    fname = "FrozenLake_" + str(k) + "_output"
    with open(fname + '.txt', 'w') as f:
        temp = str(k) + " " + str(n) + " " + str(m) + "\n"
        f.write(temp)
        for i in solution:
            for j in i:
                f.write(str(j))
            f.write("\n")

def Q_learning(maze, k, n, m):
    
    table = [[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if maze[i][j] == 'S':
                sx = i
                sy = j
            table[i][j] = {}
            for k in range(4):
                nextx = i + x[k]
                nexty = j + y[k]
                if nextx>=0 and nextx<n and nexty>=0 and nexty<m:
                    table[i][j][k] = 0

    for i in range(1000000):
        nowx = sx
        nowy = sy
        
        while maze[nowx][nowy] != 'H' and maze[nowx][nowy] != 'G':
            temp = list(table[nowx][nowy].keys())
            index = random.choice(temp)
            nextx = nowx + x[index]
            nexty = nowy + y[index]

            if maze[nextx][nexty] == 'H':
                table[nowx][nowy][index] = -1
            elif maze[nextx][nexty] == 'G':
                table[nowx][nowy][index] = 1
            else:
                table[nowx][nowy][index] = 0.5*max(table[nextx][nexty].values())

            nowx = nextx
            nowy = nexty
    
    nowx = sx
    nowy = sy
    while True:
        temp1 = list(table[nowx][nowy].keys())
        temp2 = list(table[nowx][nowy].values())
        temp = temp2.index(max(temp2))
        
        index = temp1[temp]
        
        nextx = nowx + x[index]
        nexty = nowy + y[index]
        if maze[nextx][nexty] == 'G':
            break
        maze[nextx][nexty] = 'R'

        nowx = nextx
        nowy = nexty
    
    return maze

def main():

    for i in range(1, 4):
        maze, k, n, m = open_file(i)
        solution = Q_learning(maze, k, n, m)
        write_file(solution, k, n, m)
    
if __name__ == "__main__":
    main()
