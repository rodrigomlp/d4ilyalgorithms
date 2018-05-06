death = [
    ('Jimi', 'Hendrix', 27),
    ('James', 'Dean', 24),
    ('George', 'Gershwin', 38),
]

print(sorted(death, key=lambda age: age[2]))