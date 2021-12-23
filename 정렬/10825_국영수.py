'''
도현이네반 학생 N명의 이름과 국영수 점수 3개.
성적을 정렬ㄹ하는 프로그램 작성.
국어점수가 감소하는 순서
국어점수가 같으면 영어점수가 "증가하는 순서"
국어 점수와 영어가 같으면 수학이 감소.
모든 점수가 같으면 이름이 사전순으로
'''

N = int(input())
score_list = []

for i in range(N):
    temp = input().split()

    score_list.append((temp[0], int(temp[1]), int(temp[2]), int(temp[3])))

score_list.sort(key=lambda student: (-student[1], student[2], -student[3], student[0]))

for i in score_list:
    print(i[0])