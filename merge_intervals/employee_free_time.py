from heaps import Heap
from typing import List
import heapq

class Interval(object):
    def __init__(self, start_time: int, end_time: int):
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return str(f'Interval({self.start_time}, {self.end_time})')

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.end_time < other.end_time

    def merge(self, other):
        """assuming other ends later than self"""
        if other.start_time <= self.end_time:
            return Interval(self.start_time, other.end_time)
        raise ValueError('Intervals do not overlap')


class EmployeeTimeSlot(object):
    def __init__(self, employee_index: int, time_slot_index: int, interval: Interval):
        self.employee_index = employee_index
        self.time_slot_index = time_slot_index
        self.interval = interval

    def __lt__(self, other):
        return self.interval < other.interval

    def __str__(self):
        return str(self.interval)

    def __repr__(self):
        return str(self)


def find_employee_free_time(employee_working_times: List[List[Interval]]) -> List[Interval]:
    if not employee_working_times:
        return []
    min_heap = [
        EmployeeTimeSlot(employee_index, 0, times[0])
        for employee_index, times in enumerate(employee_working_times)
    ]
    heapq.heapify(min_heap)
    running_busy_interval: Interval = min_heap[0].interval
    free_times = []
    while min_heap:
        next_free: EmployeeTimeSlot = heapq.heappop(min_heap)
        if next_free.time_slot_index < len(employee_working_times[next_free.employee_index]) - 1:
            heapq.heappush(
                min_heap,
                EmployeeTimeSlot(next_free.employee_index, next_free.time_slot_index + 1,
                                 interval=employee_working_times[next_free.employee_index][next_free.time_slot_index + 1])

            )
        try:
            running_busy_interval = running_busy_interval.merge(next_free.interval)
        except ValueError:
            free_times.append(Interval(running_busy_interval.end_time, next_free.interval.start_time))
            running_busy_interval = next_free.interval
    return free_times


if __name__ == '__main__':
    print(find_employee_free_time([
        [Interval(1, 3), Interval(9, 12)],
        [Interval(2, 4), Interval(6, 8)]
    ]))
