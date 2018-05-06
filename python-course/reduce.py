from functools import reduce

reduced = reduce(lambda x,y: x+y, [47, 11, 42, 13])

print(reduced)