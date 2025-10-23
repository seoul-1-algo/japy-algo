N, S = map(int, input().split())
nums = list(map(int, input().split()))

start_point = 0
end_point = 0
answer_length = N + 1
current_sum = nums[0]

while True:
    if current_sum < S:
        if end_point == N - 1:
            break
        end_point += 1
        current_sum += nums[end_point]
    else:
        answer_length = min(answer_length, end_point - start_point + 1)
        current_sum -= nums[start_point]
        start_point += 1

if answer_length == N + 1:
    print(0)
else:
    print(answer_length)