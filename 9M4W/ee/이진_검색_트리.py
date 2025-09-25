import sys
sys.stdin = open('5639.txt')

sys.setrecursionlimit(100000)
nums = []

while True:
    try:
        nums.append(int(input()))
    except:
        break

root = 0 # 0번째 수가 루트

left = [-1] * len(nums) # 각 노드의 왼쪽 자식 인덱스
right = [-1] * len(nums) # 각 노드의 오른쪽 자식 인덱스

# 이진 탐색 트리 만들기 !!
for i in range(1, len(nums)):

    cur = 0 # 현재 비교할 노드의 인덱스 (루트부터 시작)
    
    while True:
        # 삽입할 값이 현재 노드보다 작으면 왼쪽 서브트리로
        if nums[i] < nums[cur]:
            if left[cur] == -1: # 왼쪽 자식이 없으면
                left[cur] = i # 현재 노드를 왼쪽 자식으로 
                break
            cur = left[cur] # 왼쪽 자식으로 이동해서 계속 탐색

        # 삽입할 값이 현재 노드보다 크거나 같으면 오른쪽 서브트리로
        else:
            if right[cur] == -1: # 오른쪽 자식이 없으면
                right[cur] = i # 현재 노드를 오른쪽 자식으로
                break
            cur = right[cur] # 오른쪽 자식으로 이동해서 계속 탐색
    
# 후위 순회
def post(idx):
    if idx == -1:
        return
    post(left[idx])
    post(right[idx])
    print(nums[idx])

post(root)