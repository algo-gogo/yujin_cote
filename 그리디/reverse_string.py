# 0/1만 .. 문자열 S
# 모든 숫자 전부 같게.
# 연속된 하나 이상의 숫자를 잡고 모두 뒤집기

#0001100 -> 110011
#2. 4문자부터 5까지 뒤집으면. ㅇㅎㅇㅎ.......
#4번째부터 5번째까지 -> 1번만에.


#0001100


def solution( input ) :
    zero=0
    one=0

    before = ""

    for i in input:
        if i != before:
            if i == "0":
                zero += 1
            else:
                one += 1
            before = i
            

    print(zero)
    print(one)
    return min(zero, one)



print(solution("0110010"))