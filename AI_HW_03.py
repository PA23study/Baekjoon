def count_ways(n):

    # 돌다리 개수에 따른 방법 수 저장할 리스트
    ways = [0] * (n+1)

    # 초기값
    ways[0] = 1 

    # 동적 프로그래밍 
    for i in range(1, n+1):

        if i >= 1:
            ways[i] += ways[i-1] 
        
        if i >= 2 :
            ways[i] += ways[i-2] 

        if i >= 3:
            ways[i] += ways[i-3] 
    
    return ways[n]


t = int(input()) # 테스트 케이스 수

for _ in range(t):
    n = int(input()) # 돌다리의 개수 n

    cnt = count_ways(n)

    print(cnt % 1904101441)