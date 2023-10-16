
# # 돌다리 개수에 따른 방법 수 저장할 리스트
# ways = []

# # 초기값
# ways[0] = 1 


# def count_ways(n):
#     global ways

#     if len(ways) > n:
#         return ways[n]
    
#     # 동적 프로그래밍 
#     for i in range(1, n+1):
#         if len(ways) < i - 1:
#             temp = 0
#             if i >= 1:
#                 temp += ways[i-1] 
            
#             if i >= 2 :
#                 temp += ways[i-2] 

#             if i >= 3:
#                 temp += ways[i-3] 
#             temp %= 1904101441
#             ways.append(temp)

#     return ways[n]


# t = int(input()) # 테스트 케이스 수

# for _ in range(t):
#     n = int(input()) # 돌다리의 개수 n

#     cnt = count_ways(n)

#     print(cnt)



mem = dict()
mem[1], mem[2], mem[3] = 1, 2, 4

T = int(input())

for _ in range(T):
    n = int(input())
    
    if n not in mem and n > 3:
        for i in range(4,n+1):
            mem[i] = (mem[i-1]+mem[i-2]+mem[i-3])%1904101441
    print(mem[n])


    