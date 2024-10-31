input_str = input("Enter String: ")
char_count = {}

for char in input_str:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

for char, count in char_count.items():
    print(f"Element '{char}' is found {count} times")
