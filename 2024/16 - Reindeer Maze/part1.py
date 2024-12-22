from enum import Enum
import heapq


COST_TURN = 1000
COST_FORWARD = 1

class Dir(Enum):
    N = 0
    E = 1
    S = 2
    W = 3

    def cw(self):
        return Dir((self.value + 1) % 4)

    def ccw(self):
        return Dir((self.value - 1) % 4)

    def inv(self):
        return Dir((self.value + 2) % 4)

    def move(self):
        return ((-1, 0), (0, 1), (1, 0), (0, -1))[self.value]

    def __str__(self):
        return ('^', '>', 'v', '<')[self.value]

    def __lt__(self, other):
        return self.value < other.value


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
                start = p, Dir.E
            elif c == 'E':
                end = p
            for d in [Dir.N, Dir.E, Dir.S, Dir.W]:
                graph[p,d] = {}
                graph[p,d][p, d.cw()] = COST_TURN
                graph[p,d][p, d.ccw()] = COST_TURN
                np = p + d
                if data[np[0]][np[1]] != '#':
                    graph[p,d][np,d] = COST_FORWARD
    return graph, start, end


def display(data, path):
    def color(char):
        if char in ['S', 'E']:
            return f'\033[32m{char}\033[0m'
        elif char in ['^', '>', 'v', '<']:
            return f'\033[31m{char}\033[0m'
        else:
            return char
    grid = [[c for c in l] for l in data]
    for p, c in path:
        grid[p[0]][p[1]] = str(c)
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

    distances_end_nodes = [distances[end, d] for d in [Dir.N, Dir.E, Dir.S, Dir.W] if (end, d) in distances.keys()]
    score = min(distances_end_nodes)

    path = []
    current = end, [Dir.N, Dir.E, Dir.S, Dir.W][distances_end_nodes.index(score)]
    while current is not None:
        path.append(current)
        current = parents[current]
    path.reverse()
    return path, score


# def dist_L1(p1, p2):
#     return (abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])) * COST_FORWARD
#
#
# def astar(graph, start, end, h):
#     distances = {p: float('inf') for p in graph.keys()}
#     distances[start] = 0
#     parents = {node: None for node in graph}
#
#     hq = [(h(start, end), start)]
#     heapq.heapify(hq)
#     while hq:
#         h_dist, node = heapq.heappop(hq)
#         if node[0] == end:
#             break
#
#         for neighbor in graph[node].keys():
#             tentative_dist = distances[node] + graph[node][neighbor]
#             if tentative_dist < distances[neighbor]:
#                 distances[neighbor] = tentative_dist
#                 parents[neighbor] = node
#                 heapq.heappush(hq, (tentative_dist + h(neighbor, end), neighbor))
#
#     distances_end_nodes = [distances[end, d] for d in [Dir.N, Dir.E] if (end, d) in distances.keys()]
#     score = min(distances_end_nodes)
#
#     path = []
#     current = end, [Dir.N, Dir.E][distances_end_nodes.index(score)]
#     while current is not None:
#         path.append(current)
#         current = parents[current]
#     path.reverse()
#     return path, score


def main(data):
    graph, start, end = build_graph(data)
    path = []
    path, score = dijkstra(graph, start, end)
    # path, score = astar(graph, start, end, dist_L1)
    # display(data, path)
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
