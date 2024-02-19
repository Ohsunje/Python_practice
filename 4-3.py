
key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}
for i in range(4):
    character[key_list[i]] = value_list[i]
    print(character)
print(character)

"""
limit = 10000
i = 1
answer = 0
while (1):
    answer += i
    i += 1
    if answer > limit:
        break;

print(i, answer)
"""

"""
max_value = 0
a = 0
b = 0

for i in range(1, 101):
    j = 100 - i
    max_value = i * j
    if max_value < (i +1) * (j - 1):
        i += 1
    else:
        a = i
        b = j
        break

print(a, b, max_value)
"""