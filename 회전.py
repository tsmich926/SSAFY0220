T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    ss = list(input().split())
    i = 0
    while i < M:
        a = ss.pop(0)
        ss.append(a)
        i += 1
    ans = ss[0]
    print(f'#{tc} {ans}')