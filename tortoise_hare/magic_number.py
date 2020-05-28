def next_(num: int) -> int:
    ans = 0
    while num > 0:
        ans += (num % 10) ** 2
        num //= 10
    return ans


def is_magic_number(num: int) -> bool:
    """Given a positive integer, return if the number is a magic number"""
    if num == 0:
        return False
    if num == 1:
        return True
    slow = num
    fast = next_(num)
    while slow != fast:
        if slow == 1 or fast == 1:
            return True
        slow = next_(slow)
        fast = next_(next_(fast))
    return False


if __name__ == '__main__':
    print(is_magic_number(12))