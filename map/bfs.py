def bfs(_map: list, start_pos: list, end_pos: list) -> list:
    print("running")
    def is_valid(_pos: list) -> bool:
        if 0 <= _pos[0] < len(_map) and 0 <= _pos[1] < len(_map[0]) and \
             _map[_pos[0]][_pos[1]] == 0 and stat[_pos[0]][_pos[1]][0] == -1:
            return True
        return False
    stat = [[[-2 if _map[j][i]==1 else -1, -1] for i in range(len(_map[0]))] for j in range(len(_map))]
    stat[start_pos[0]][start_pos[1]] = [4, -1]
    move = [[0,-1], [-1,0], [0,1], [1,0]]
    queue = [start_pos]
    while queue: # BFS
        top = queue.pop()
        for i in range(4):
            nxt = [top[0]+move[i][0], top[1]+move[i][1]]
            if not is_valid(nxt):
                continue
            stat[nxt[0]][nxt[1]] = [stat[top[0]][top[1]][0] + 1, i]
            if nxt == end_pos:
                break
            queue = [nxt] + queue
    path, direction = [], []
    pos = end_pos
    cnt = 0
    while True: # 获取路径
        i = stat[pos[0]][pos[1]][1]
        path = [pos] + path
        direction = [i] + direction
        if pos == start_pos:
            break
        i = (i + 2) % 4
        pos = [pos[0]+move[i][0], pos[1]+move[i][1]]
    return path, direction[1:]

if __name__ == "__main__":
    a = [[1,0,0,0,0,0],
         [1,0,1,0,1,0],
         [0,0,1,1,1,0],
         [0,1,0,0,0,0],
         [0,0,0,1,0,0]]
    print(bfs(a, [1,3], [4,4])[0])
