# q = []
# m=20
# no = 1
# q.append(no,1) #1번줄마이쭈한개
# curno,curmy = a.pop(0) #1번줄 받아감
# q.append(curno,curmy+1) #1번줄 마이쭈2개
# #1번이 줄을서고 받아서 다시 줄을서는과정
#
# no += q.append(no) #2번줄
# curno = a.pop(0) #1번줄
# q.append(curno) #1번이 받아감
# no += 1
# q.append(no) 3번줄(

# inque는 append()
# deque는 pop(0)
# popleft()
# front,rear


q = []
m = 20
no = 1
q.append((no, 1))
total = 0
while q:
    curno, curmy = q.pop(0)  # 1번줄 받아감
    total += curmy
    print(curno,curmy,total)
    if total >= 20:
        break
    q.append((curno, curmy + 1))  # 1번줄 마이쭈2개
    no += 1
    q.append((no,1))