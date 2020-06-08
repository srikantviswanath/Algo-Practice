from typing import List


def jump(index: int, array: List[int]) -> (bool, int):
    val = array[index]
    temp = index + val
    return temp >= len(array), temp % len(array)


def is_cycle_present(arr: List[int]) -> bool:
    """
    We are given an array containing positive and negative numbers. Suppose the array contains a number ‘M’ at a particular index. Now, if ‘M’ is positive we will move forward ‘M’ indices and if ‘M’ is negative move backwards ‘M’ indices. You should assume that the array is circular which means two things:

    If, while moving forward, we reach the end of the array, we will jump to the first element to continue the movement.
    If, while moving backward, we reach the beginning of the array, we will jump to the last element to continue the movement.
    Write a method to determine if the array has a cycle. The cycle should have more than one element and should follow one direction which means the cycle should not contain both forward and backward movements.
    """
    if not arr or len(arr) == 1:
        return False
    wrapped = False
    slow = 0
    _, fast = jump(slow, arr)
    while slow != fast:
        _, slow = jump(slow, arr)
        temp_wrapped, fast = jump(fast, arr)
        wrapped |= temp_wrapped
        temp_wrapped, fast = jump(fast, arr)
        wrapped |= temp_wrapped
    if jump(slow, arr)[1] == fast:  # cycle of 1 element
        return False
    return wrapped


if __name__ == '__main__':
    print(is_cycle_present([2, 1, -1, -2]))