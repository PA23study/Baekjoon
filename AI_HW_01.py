import bisect


def func(q, k, nlist): # [q-k, q+k]에 속하는 nlist 원소의 개수를 찾는 함수

    cnt = 0

    # bisect_left(list, target): 정렬된 리스트에서 target을 insert 할 때의 위치
    index_left = bisect.bisect_left(nlist, q-k) 
    index_right = bisect.bisect_right(nlist, q+k) 

    cnt = index_right - index_left
    
    return cnt 


t = int(input())

for _ in range(t):
    k = int(input()) # 쿼리와의 차이가 최대 K인 숫자들 찾기

    nlist = list(map(int, input().split())) # 정렬된 리스트 입력

    m = list(map(int, input().split())) # 쿼리 입력, 해당 쿼리와의 차이가 최대 K인 숫자 개수 찾기
    
    cnt = 0
    for q in m :
        # [q-k, q+k] 에 속하는 리스트 원소의 개수를 찾아야 함
        cnt += func(q, k, nlist)
    
    print(cnt)
