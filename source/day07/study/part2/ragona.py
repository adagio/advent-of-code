# https://gist.github.com/ragona/5ed963ecd4153d0625612f403ae332d1

import re
import heapq
import unittest
from string import ascii_uppercase
from collections import defaultdict, deque


log_parser = re.compile(" (.) .+ (.) ")
pairs = [log_parser.search(line.strip()).groups() for line in open("input/day_07.txt").readlines()]


BASE_COST = 60
DEBUG = True


def make_graph():
    graph = Graph()
    for a, b in pairs:
        graph.connect(a, b)
    return graph


class Graph:

    class Node:

        def __init__(self, data=None):
            self.data = data
            self.indegree = 0
            self.children = set()

        def __hash__(self):
            return hash(self.data)

        def __eq__(self, other):
            return self.data == other.data

        def __lt__(self, other):
            return self.data < other.data

        def __repr__(self):
            return f"Node(" \
                f"data={self.data}, " \
                f"indegree={self.indegree}, " \
                f"children=({''.join(n.data for n in sorted(self.children))}))"

        @property
        def cost(self):
            return ascii_uppercase.find(self.data) + 1 + BASE_COST

    def __init__(self):
        self.nodes = defaultdict(Graph.Node)

    def __getitem__(self, item):
        node = self.nodes[item]
        if node.data is None:
            node.data = item

        return node

    def connect(self, a, b):
        node_a = self[a]
        node_b = self[b]
        node_a.children.add(node_b)
        node_b.indegree += 1


class Worker:
    def __init__(self):
        self.job = None
        self.remaining_cost = 0

    def __repr__(self):
        if not self.job:
            return " . "
        return f" {self.job.data} "

    @property
    def free(self):
        return not self.job or self.remaining_cost == 0

    def set_job(self, job):
        self.job = job
        if job:
            self.remaining_cost = job.cost

    def work(self):
        if self.job and self.remaining_cost > 0:
            self.remaining_cost -= 1


def time_with_workers(graph, num_workers=5):
    workers = [Worker() for _ in range(num_workers)]
    work_queue = deque(list(find_graph_order(graph)))  # todo: after a refactor I don't think this needs to be a deque
    total_seconds = 0
    done = set()  # used for debug drawing
    in_progress = set()

    def work():
        for worker in workers:

            if not worker.free:
                worker.work()

            elif worker.free:

                if worker.job and worker.job in in_progress:
                    in_progress.remove(worker.job)
                    done.add(worker.job)

                new_job = next_job()
                if new_job:
                    in_progress.add(new_job)

                worker.set_job(new_job)
                worker.work()  # do one round of work immediately on the new job

    def next_job():
        if not work_queue:
            return None

        seen = set()
        for potential_job in work_queue:
            seen.add(potential_job)
            if node_is_ready(potential_job, blockers=seen | in_progress):
                work_queue.remove(potential_job)
                return potential_job

        return None

    def node_is_ready(potential_job, blockers):
        for node in blockers:
            if potential_job in node.children:
                return False
        return True

    work()  # example has one round of work before the 0th second. I think this is causing an off-by-one for me.

    while work_queue or in_progress:
        work()
        total_seconds += 1

    return total_seconds


def simple_graph():
    """
    Test case graph from the challenge text.
    """
    graph = Graph()
    graph.connect("C", "A")
    graph.connect("C", "F")
    graph.connect("A", "B")
    graph.connect("A", "D")
    graph.connect("B", "E")
    graph.connect("D", "E")
    graph.connect("F", "E")
    return graph


def find_graph_order(graph):
    ready = sorted([node for node in graph.nodes.values() if node.indegree == 0])

    while ready:
        node = heapq.heappop(ready)

        for child in sorted(node.children):
            child.indegree -= 1
            if child.indegree == 0:
                heapq.heappush(ready, child)

        yield node


def main():

    print("Part 1:", ''.join([node.data for node in find_graph_order(make_graph())]))

    print("Part 2:", time_with_workers(make_graph()))


if __name__ == '__main__':
    main()


class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = simple_graph()

    def test_graph_order(self):
        order = find_graph_order(self.graph)
        assert ''.join([node.data for node in order]) == 'CABDFE'

    def test_time_with_workers(self):
        global BASE_COST
        BASE_COST = 0
        time = time_with_workers(self.graph, 2)
        assert time == 15

