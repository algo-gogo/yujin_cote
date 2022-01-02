'''
또 지대 짱나는 카카오 문제
노래 가사에 특정 키워드가 몇 개 포함되어 있는지 검색하는 프로그램.
와일드카드;;; 아놔 ㅋㅋ 역시고만고만하게내지않죠?

예를 들어 "fro??"는 "frodo", "front", "frost" 등에 매치되지만 "frame", "frozen"에는 매치되지 않습니다.

가사에 사용된 모든 단어들이 담긴 배열 words와 찾고자 하는 키워드가 담긴 배열 queries가 주어질 때,
각 키워드 별로 매치된 단어가 몇 개인지 순서대로 배열에 담아 반환하도록 solution 함수를 완성해 주세요.

단어 자체의 중복은 없는걸로 가정함.
'''
def find_wildcard_end(word, start, end, last=-1):
    mid = (start + end) // 2

    if( start>end ):
        return last
    elif( word[mid] == "?" ):
        last = mid
        return find_wildcard_end(word, mid+1, end, last)
    else:
        return find_wildcard_end(word, start, mid-1, last)

def check(word, query, start=0):
    # print( query, index )
    if len(word) != len(query):
        return False

    for i in range(start,len(word)):
        if query[i] == "?":
            return True
        elif query[i] != word[i]:
            return False

    return True

def solution(words, queries):
    answer = []

    for query in queries:
        # print(query)
        count = 0
        index = 0

        if( query[0] == "?" ):
            index = find_wildcard_end(query, 0, len(query)-1) + 1

        for word in words:
            if (check(word, query, index)):
                count += 1

        answer.append(count)

    return answer

print( solution([
    "frodo", "front", "frost", "frozen", "frame", "kakao"],
    ["?????"]
    )
)