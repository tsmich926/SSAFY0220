def amho(bb):
    n = 1
    while True:
        if n == 6:
            n = 1
        t = bb.pop(0)
        t = t - n
        if t <= 0:
            bb.append(0)
            return bb
            break

        else:  # t가 0보다큰경우
            bb.append(t)
            n += 1



for tc in range(1,11):
    N = int(input())
    bb = list(map(int,input().split()))

    ans = amho(bb)


    # print(f'#{tc}', end=" ")
    # print(*ans)



    print(f'#{tc}', end=" ")
    for i in ans:
        print(i, end= ' ')
    print()





    # lst = [10,6,12,8,9,4,1,3]
    # t= lst.pop()
    # t -= 1
    # if t <= 0:
    #
    #
    # value = 1
    # while
    #     t = lst.pop(0)
    #     t -= value
    #     if t<= 0:
    #
    #     value = (value+1)%5+1
