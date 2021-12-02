'''
카카오 문제
어피치깅은 문자열을 압축
비손실 압축 문자 반복 빈도로 표시
그런데 반복안되면 구림.
여러개 단위로 자르기. 제일짧은거 ""길이"" 리턴하도록.
'''

def solution(s):
    result = ""

    cut = 1

    min_value = len(s)
    while cut < int(len(s)/2)+1:
        count = 1
        last_character = ""
        mod = len(s) % cut

        for i in range(0,len(s),cut):
            temp = s[i:i+cut]
            if i == 0:
                last_character = temp
                continue
            elif last_character == temp:
                count += 1

                if i == len(s)-cut:
                    if( count > 1 ):
                        result += str(count)
                    result += last_character
                    last_character = temp
                    count = 1
            elif last_character != temp:
                if( count > 1 ):
                    result += str(count)
                result += last_character
                last_character = temp
                if i == len(s)-cut:
                    result += last_character
                count = 1

        if mod > 0:
            result += s[i:]
        count = 1
        cut += 1
        min_value = min(min_value,len(result))
        print(result)
        result = ""

    return(min_value)



solution("ababcdcdababcdcd")            
