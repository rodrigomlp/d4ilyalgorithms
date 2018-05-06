dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]

print(list(map(lambda x : x['name'], dict_a))) # Output: ['python', 'java']
print(list(map(lambda x : x['points']*10,  dict_a))) # Output: [100, 80]

print(list(map(lambda x : x['name'] == "python", dict_a))) # Output: [True, False]