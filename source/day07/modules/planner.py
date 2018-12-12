def get_time(steps, workers_n, base_time=60):
    """
    Given steps graph and number of workers
    Returns time for work to be completed
    Based on code by u/marhoy
    https://www.reddit.com/r/adventofcode/comments/a3wmnl/2018_day_7_solutions/ebgd6oc/
    """

    # Add amount of work for each node
    for node in steps.nodes:
        steps.nodes[node]['work'] = ord(node) - ord('A') + 1 + base_time

    time = 0
    while steps.nodes:
        # Find nodes available for work
        # If there are 0 edges pointing in to the node
        # it is, previous steps have been removed
        available_nodes = [node for node in steps.nodes if steps.in_degree(node) == 0]
        
        # Sort available nodes in alphabetical order
        available_nodes.sort()
        
        # Reduce remaining work for workers_n of the available nodes
        for worker, node in zip(range(workers_n), available_nodes):
            steps.nodes[node]['work'] -= 1  # print(f'{time}: Worker {worker} is on task {node}')
            # Remove finished nodes
            if steps.nodes[node]['work'] == 0:
                steps.remove_node(node)  # print(f'{time}: Node {node} is finished!')

        # Increase time
        time += 1

    return time

