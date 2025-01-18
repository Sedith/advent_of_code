from collections import defaultdict


def find_3cliques(graph):
    cliques = set()

    for node in graph:
        neighbors = list(graph[node])
        for i, n1 in enumerate(neighbors):
            for n2 in neighbors[i + 1 :]:  # pairs before i + 1 are already checked
                if n2 in graph[n1]:
                    cliques.add(tuple(sorted([node, n1, n2])))

    return list(cliques)


def main(data):
    ## build connection graph
    connections = defaultdict(set)
    for connection in data:
        cpt1, cpt2 = connection.split('-')
        connections[cpt1].add(cpt2)
        connections[cpt2].add(cpt1)

    return sum([1 for c in find_3cliques(connections) if any([cpt.startswith('t') for cpt in c])])


if __name__ == '__main__':
    import sys
    import time

    tic = time.time()
    file = 'input.txt' if sys.argv[1:] else 'example.txt'
    with open(file, 'r') as f:
        data = f.read().splitlines()
    result = main(data)
    toc = time.time()
    print(f'result   : {result}')
    print(f'time [s] : {toc - tic:.5f}')
