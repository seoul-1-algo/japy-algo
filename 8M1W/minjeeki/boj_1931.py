N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x: (x[1], x[0]))
cnt = 1
cur_meeting = meetings[0]
for meeting in meetings[1:]:
    if cur_meeting[1] <= meeting[0]:
        cur_meeting = meeting
        cnt += 1
print(cnt)