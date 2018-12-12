def get_time(steps, workers_n):
    """
    Given steps graph and number of workers
    Returns time for work to be completed
    Based on code by u/marhoy
    https://www.reddit.com/r/adventofcode/comments/a3wmnl/2018_day_7_solutions/ebgd6oc/
    """

    # Add amount of work for each node
    for node in steps.nodes:
        steps.nodes[node]['work'] = ord(node) - ord('A') + 1 + 60

    time = 0
    while steps.nodes:
        # Find nodes available for work
        available_nodes = [node for node in steps.nodes if steps.in_degree(node) == 0]
        
        # Sort available nodes: Work on nodes with least remaining work
        available_nodes.sort(key=lambda node: steps.nodes[node]['work'])
        
        # Reduce remaining work for workers_n of the available nodes
        for worker, node in zip(range(workers_n), available_nodes):
            # print(f'{time}: Worker {worker} is on task {node}')
            steps.nodes[node]['work'] -= 1

            # Remove finished nodes
            if steps.nodes[node]['work'] == 0:
                # print(f'{time}: Node {node} is finished!'))
                steps.remove_node(node)

        # Increase time
        time += 1

    return time

