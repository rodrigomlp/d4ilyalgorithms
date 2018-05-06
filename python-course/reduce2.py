from functools import reduce

list = [10, 6, 7, 11, 2, 1, 8, 5]
#S = reduce(lambda x, y: x if x > y else y, list)
print(max(list))
