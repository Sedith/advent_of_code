from enum import Enum
import heapq


class Dir(Enum):
    N = 0
    E = 1
    S = 2
    W = 3

    def move(self):
        return ((-1, 0), (0, 1), (1, 0), (0, -1))[self.value]

    def __str__(self):
        return ('^', '>', 'v', '<')[self.value]


class Pos(tuple):
    def __new__(cls, i, j):
        return super(Pos, cls).__new__(cls, (i, j))

    def __add__(self, d):
        di, dj = d.move()
        return Pos(self[0] + di, self[1] + dj)


def build_graph(data):
    graph = {}
    for i, l in enumerate(data):
        for j, c in enumerate(l):
            if c == '#':
                continue
            p = Pos(i, j)
            if c == 'S':
                start = p
            elif c == 'E':
                end = p
            graph[p] = {}
            for d in [Dir.N, Dir.E, Dir.S, Dir.W]:
                np = p + d
                if data[np[0]][np[1]] != '#':
                    graph[p][np] = 1
    return graph, start, end


def display(data, path):
    def color(char):
        if char in ['S', 'E']:
            return f'\033[32m{char}\033[0m'
        elif char in ['x']:
            return f'\033[31m{char}\033[0m'
        elif char == '.':
            return ' '
        else:
            return char

    grid = [[c for c in l] for l in data]
    for p in path[1:-1]:
        grid[p[0]][p[1]] = 'x'
    print(''.join([''.join([color(c) for c in l]) + '\n' for l in grid]))


def dijkstra(graph, start, end):
    distances = {p: float('inf') for p in graph.keys()}
    distances[start] = 0
    parents = {node: None for node in graph}

    hq = [(0, start)]
    heapq.heapify(hq)
    while hq:
        dist, node = heapq.heappop(hq)
        if dist > distances[node]:
            continue

        for neighbor in graph[node].keys():
            tentative_dist = dist + graph[node][neighbor]
            if tentative_dist < distances[neighbor]:
                distances[neighbor] = tentative_dist
                parents[neighbor] = node
                heapq.heappush(hq, (tentative_dist, neighbor))

    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parents[current]
    path.reverse()
    return path, len(path)


def dist_L1(p1, p2):
    return (abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])) * 1


def astar(graph, start, end, h):
    distances = {p: float('inf') for p in graph.keys()}
    distances[start] = 0
    parents = {node: None for node in graph}

    hq = [(h(start, end), start)]
    heapq.heapify(hq)
    while hq:
        _, node = heapq.heappop(hq)
        if node == end:
            break

        for neighbor in graph[node].keys():
            tentative_dist = distances[node] + graph[node][neighbor]
            if tentative_dist < distances[neighbor]:
                distances[neighbor] = tentative_dist
                parents[neighbor] = node
                heapq.heappush(hq, (tentative_dist + h(neighbor, end), neighbor))

    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parents[current]
    path.reverse()
    return path, len(path)


def main(data):
    graph, start, end = build_graph(data)
    path, score = dijkstra(graph, start, end)
    # path, score = astar(graph, start, end, dist_L1)
    display(data, path)
    return score


if __name__ == '__main__':
    import sys
    import time

    tic = time.time()
    file = 'input.txt' if sys.argv[1:] else 'example2.txt'
    with open(file, 'r') as f:
        data = f.read().splitlines()
    result = main(data)
    toc = time.time()
    print(f'result   : {result}')
    print(f'time [s] : {toc - tic:.5f}')
