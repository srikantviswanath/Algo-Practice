def triplet_sum_close_to_target(arr, target_sum):
  """
  Given an unsorted array of integers and a target sum, find a unique triplet whose sum
  is closest to the given target sum. If more than one such triplet exists, return the
  sum of the smallest triplet
  """
  if not arr:
    return 
  arr.sort()
  ans = float('inf')
  min_diff = float('inf')
  for first, num in enumerate(arr):
    second = first + 1
    third = len(arr) - 1
    while second < third:
      total = arr[first] + arr[second] + arr[third]
      diff = abs(target_sum - total)
      if diff == min_diff:
        ans = min(ans, total)
      elif diff < min_diff:
        min_diff = diff
        ans = total
      if total > target_sum:
        third -= 1
      elif total < target_sum:
        second += 1

  return ans
