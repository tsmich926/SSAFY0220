# T =int(input())
# for tc in range(1,T+1):
#     N,M = map(int,input().split())
#     ci = [0] + list(map(int,input().split()))
#     oven= [0]*N
#
#     while oven에 피자가 있는동안:
#         no,c = oven.pop(0) #1화덕 피자치즈량
#         반으로
#         if 치즈량 >0:
#             oven.append((no,치즈량))
#             다시 오븐에
#         else:
#             oven.append(next피자번호,치즈량) #다음피자를 오븐에


T =int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    ci = [0] + list(map(int,input().split()))
    oven= [(0,0)]*N #치즈량이 0인 피자들이 화덕에 N개 들어있다. 0번피자들이 꽉 차있다.(초기화)

    nextp= 1
    while oven: #치즈량이 0인 피자들이 차있음
        no,c = oven.pop(0) #0번 피자가 빠져나옴 0,0
        c //= 2 #치즈량이 0이므로  c는 0보다 작겠지
        if c > 0:
            oven.append((no,c)) #다시 오븐에 넣고
        else:
            if nextp <= M: # 처음 np는 1이므로 m보다 작고
                oven.append((nextp,ci[nextp])) #1번피자를 치즈1번양 채워서 오븐에 넣는다
                nextp += 1
    print(f'#{tc} {no}')


     #for 루프로 피자를 채우고 시작해도 됨