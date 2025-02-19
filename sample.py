# queue = [0] * 3
# front = rear = -1       # 다른 방식도 있지만, 우리는 꺼내거나 삽입할 때마다 위치 변경할거라

# # 1, 2, 3 인큐
# rear += 1
# queue[rear] = 1

# rear += 1
# queue[rear] = 2

# rear += 1
# queue[rear] = 3

# # 디큐 세 번
# while front != rear:
#     front += 1
#     t = queue[front]
#     print(t)
    
# print(queue)

# # front += 1
# # print(queue[front])

# # front += 1
# # print(queue[front])

# # front += 1
# # print(queue[front])

# q = []
# q.append(1)     # enqueue에 해당
# print(q)
# q.append(2)
# print(q)
# q.append(3)
# print(q)
# print(q.pop(0)) # dequeue에 해당
# print(q.pop(0))
# print(q.pop(0))

############################

from collections import deque

q = deque()
q.append(1)
q.append(2)
t = q.popleft()
print(t)
t = q.popleft()
print(q)

######################
QSIZE = 4
Q = [0] * QSIZE
front = rear = -1       # 선형큐의 초기값, head tail도 사용

def enqueue(item):
    if rear == QSIZE -1:
        print("over")
        return
    global rear
    rear += 1
    Q[rear] = item

def dequeue():
    global front
    if front == rear:
        print("under")
        return
    front += 1
    return Q[front]

