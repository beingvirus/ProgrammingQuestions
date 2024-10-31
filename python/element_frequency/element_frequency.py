lst = ['1', 'a', '22', 'b', '12', '12', '12', '23', '21', 'a', 'b']

frequency = {}

for element in lst:
    if element in frequency:
        frequency[element] += 1
    else:
        frequency[element] = 1
print(frequency)
for element, count in frequency.items():
    print(f"Element '{element}' is found {count} times")
