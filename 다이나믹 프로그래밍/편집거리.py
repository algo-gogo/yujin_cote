'''
두개의 문자열 A, B가 주어졌을 때 A->B로 만드려 함
한번에 삽입, 삭제, 교체 중 하나가 가능.
편집거리 = 필요한 연산의 수
1 <= N <= 5000

얼마나 다른지를 체크하면 되는 건가?
'''

# n = int(input())

a = list(input())
b = list(input())

d = [[0] * (len(b)+1) for i in range(len(a)+1)]

n = 0

a_cursor = 1
b_cursor = 1

for i in range(1,len(a)+1):
    d[i][0] = i

for i in range(1,len(b)+1):
    d[0][i] = i

for r in d:
    print( r )

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if b[j-1] == a[i-1]:
            # if( i==j ):
            d[i][j] = d[i-1][j-1]
            # break
        else:
            d[i][j] = 1 + min(d[i][j - 1], d[i - 1][j], d[i - 1][j - 1])
            # continue


for r in d:
    print( r )


print(d[len(a)][len(b)])

'''
abcde
de

abdcde
de
'''