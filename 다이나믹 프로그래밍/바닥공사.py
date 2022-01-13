'''
가로 길이 N 세로 길이 2 직사각형 형태 바닥
1*2 덮ㅌ개, 2*1 덮개, 2*2 덮개
바닥을 채우는 모든 경우의 수를 구하는 프로그램

3인경우
1:3
1:1 3:1
3:1 1:1
2:2 1:1
1:1 2:2

1 / 2로 쪼갬
1을 구성하는 법 - 1짜리
2를 구성하는 법 - 2짜리 2개 2*2짜리 1개
첫번째에 1이 올 수도 있고 2가 올 수도 있다
(1*3) + (3*1) = 6?? 왜 5지

4인 경우
2 / 2 인 경우 3 * 3 = 9
1 / 2 / 1인 경우 - 3에서 1빼면 2

5일 때는 21
2로쪼개면 1/2/2 2/2/1 2/1/2가 됨
3*1*3 1*3*3 3*3*1
3*9 = 27 -> -6은 어디서 나온 값? 중복을 빼야 하는거같은데

최초에 3가지 방법이 있음.
1로시작하든가 2-1로 시작하든가 2-2로 시작하든가
그러면 3.
그다음 남은공간에도마찬가지..?..모르겠는ㄴ데

모르겟고 다시생각

3 -> 2+1인경우 1+2인경우 1+2인경우로 나눔
그러면 3 / 1 / 1이므로 5이다

아하..

'''

N = int(input())

d = [0] * 1001

d[1] = 1
d[2] = 3

for i in range(3,N+1):
    d[i] = d[i-2] + d[i-2] + d[i-1]

print( d[N] )
