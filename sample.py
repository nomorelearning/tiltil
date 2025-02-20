# class_01 = [
#     '권예경',
#     '김강산',
#     '김봉주',
#     '김서영',
#     '김준혁',
#     '김효준',
#     '문빈',
#     '박수아',
#     '박수정',
#     '신재은',
#     '안다빈',
#     '연제현',
#     '유경민',
#     '윤주현',
#     '이윤동',
#     '이효은',
#     '임태원',
#     '최수빈',
#     '최이설',
#     '하다예',
#     '현지우',
#     '황희준'
# ]
#
# import


# from collections import deque
#
# def BFS(G,v,n):
#     visited = [0]*(n+1)
#     queue = []
#     queue.append(v)
#     visited[v] = 1
#     while queue:
#         t = queue.pop(0)
#         visited(t)
import sys
sys.stdin = open('in.txt')
di = [0,1,0,-1]
dj = [1,0,-1,0]

def bfs(i,j,N):
    visited = [[0]*N for _ in range(N)]
    q = []
    q.append((i,j))
    visited[i][j] = 1
    while q:
        ti, tj = q.pop(0)
        if maze[ti][tj] == '3':
            return visited[ti][tj] - 2
        for d in range(4):
            wi, wj = ti+di[d], tj+dj[d]
            if 0<=wi<N and 0<=wj<N and maze[wi][wj] != '1' and visited[wi][wj] == 0:
                q.append((wi,wj))
                visited[wi][wj] = visited[ti][tj] + 1
    else:
        return 0



def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                return i, j

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]

    si, sj = find_start(N)
    ans = bfs(si,sj,N)
    print(f'#{tc} {ans}')
