#반나눠서 검색

def sejegop(N):
    for i in range(N):
        n = i*i*i
        if n == N:
            return n
    else:
        return -1

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    ans = sejegop(N)
    print(f'#{tc} {ans}')