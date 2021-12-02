def lucky_straight(n):
    number_list = []

    i = 1
    while i < n:
        temp = int(n/i)%10
        number_list.append(temp)
        i *= 10

    # print(number_list)

    half_index = int(len(number_list)/2)

    if( sum(number_list[:half_index]) == sum(number_list[half_index:])):
        return "LUCKY"
    else:
        return "READY"

print(lucky_straight(int(input())))