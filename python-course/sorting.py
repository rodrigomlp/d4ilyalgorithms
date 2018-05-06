d = {"a": 2, "b": 0, "c": 1}

#a = [[1,3], [8,10], [15,18], [2,6]]
print([i[0] for i in sorted(d.items(), key=lambda x: x[1])])