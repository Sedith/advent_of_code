from collections import defaultdict


def bron_kerbosch(graph, r, p, x):
    ## terminal case
    if not p and not x:
        return [r]

    cliques = []
    for v in list(p): # iterate over a copy of p since its modified
        cliques += bron_kerbosch(
            graph,
            r.union(set([v])),
            p.intersection(graph[v]),
            x.intersection(graph[v])
        )
        p.remove(v)
        x.add(v)

    return cliques


def main(data):
    ## build connection graph
    connections = defaultdict(set)
    for connection in data:
        cpt1, cpt2 = connection.split('-')
        connections[cpt1].add(cpt2)
        connections[cpt2].add(cpt1)

    cliques = bron_kerbosch(connections, set(), set(connections.keys()), set())
    lan = max(cliques, key=lambda x: len(x))

    return ''.join([f'{c},' for c in sorted(list(lan))])[:-1]



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
