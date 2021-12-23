'''
일직선 상의 마을에 여러 채의 집이 위치해있다.
이중에서 특정 위치의 집에 특별히 한개의 안테나. ㅇㅋㅇㅋ
모든 집까지의 거리의 총 합이 최소가 되도록. 치킨집문제아녀??
논리적으로 동일한 위치에 여러개의 집이 존재하는것이 가능. <- 같은위치에값을보관할수있어야됨
'''

N = int(input())
house_list = list(map(int, input().split()))

# house_list.sort()

# total = 0
# for i in house_list:
#     total += i

# print( total // len(house_list) )

min_value = 0
house_list.sort()
index = 0
for i in house_list[0:len(house_list)//2]:
    total = 0
    for j in house_list:
        total += abs(j-i)

    if (min_value == 0):
        min_value = total
        index = i
    elif min_value > total:
        min_value = total
        index = i
    
print( index )

'''
1 1 5
1+1+5 = 7
7//3 = 2
'''