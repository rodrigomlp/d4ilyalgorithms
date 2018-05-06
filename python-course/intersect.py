from functools import reduce

input_list = [[1,2,3,4,5], [2,3,4,5,6], [3,4,5,6,7]]
print(list(map(set, input_list)))
result = list(reduce(set.intersection, map(set, input_list)))
#print(result)