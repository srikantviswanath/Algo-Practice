from heaps import Heap
from typing import List


class Job(object):
    def __init__(self, start, end, load):
        self.start = start
        self.end = end
        self.load = load

    def __lt__(self, other):
        return self.end < other.end


def find_max_cpu_load(jobs: List[Job]):
    """

    We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running. Our goal is
    to find the maximum CPU load at any time if all the jobs are running on the same machine.
    """
    min_heap = Heap([])
    jobs.sort(key=lambda job: job.start)
    current_load, max_load = 0, 0

    for job in jobs:
        while min_heap.length > 0 and min_heap.min.end < job.start:
            current_load -= min_heap.min.load
            min_heap.pop()

        min_heap.push(job)
        current_load += job.load
        max_load = max(max_load, current_load)
    return max_load


if __name__ == '__main__':
    print(find_max_cpu_load([Job(1, 4, 2), Job(2, 4, 1), Job(3, 6, 5)]))