N = int(input())

card_list = []

for i in range(N):
    card_list.append(int(input()))

card_list.sort()

total = 0
for i in range(0, N, 2):
    result = 0
    for j in card_list[i:i+2]:
        result += j
    total += result

print(total)