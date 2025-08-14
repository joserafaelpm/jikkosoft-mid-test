# -*- coding: utf-8 -*-

def find_indices_of_sum(numbers, result):
  try:
    if not isinstance(numbers, list):
      return "Numbers deben ser una lista."
    if not isinstance(result, int):
      return "Result debe ser un numero."
    positions = {}
    for i, num in enumerate(numbers):
      if not isinstance(num, int):
        return "Numbers deben ser una lista de numeros"
      total = result - num
      if total in positions:
        return [positions[total], i]
      positions[num] = i
    return []
  except Exception as e:
    return f"Error: {e}"

nums = [20, 7, 11, 2]
target = 9
indices = find_indices_of_sum(nums, target)
print(f"Los indices de dos numeros que suman: {target} son: {indices}")

nums2 = [3, 2, 4]
target2 = 6
indices2 = find_indices_of_sum(nums2, target2)
print(f"Los indices de dos numeros que suman: {target2} son: {indices2}")

nums3 = [3, 3]
target3 = 6
indices3 = find_indices_of_sum(nums3, target3)
print(f"Los indices de dos numeros que suman: {target3} son: {indices3}")

nums4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5]
target4 = 10
indices4 = find_indices_of_sum(nums4, target4)
print(f"Los indices de dos numeros que suman: {target4} son: {indices4}")

nums5 = [1, 1]
target5 = 0
indices5 = find_indices_of_sum(nums5, target5)
print(f"Los indices de dos numeros que suman: {target5} son: {indices5}")

nums6 = ['1','2']
target6 = 0
indices6 = find_indices_of_sum(nums6, target6)
print(f"Los indices de dos numeros que suman: {target6} son: {indices6}")

nums7 = [1,2]
target7 = 'x'
indices7 = find_indices_of_sum(nums7, target7)
print(f"Los indices de dos numeros que suman: {target7} son: {indices7}")