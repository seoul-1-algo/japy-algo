n,m = map(int,input().split())

nums = list(map(int,input().split()))

nums = sorted(list(set(nums)))
total_nums = len(nums)

def choose(wanna_choose, lastnum_idx, choosed):
    if wanna_choose <= 0:
        print(*choosed)
        return
    if lastnum_idx >= total_nums:
        return
    # 고른 경우 함수 호출
    choosed.append(nums[lastnum_idx])
    choose(wanna_choose-1, lastnum_idx, choosed)
    
    choosed.pop()
    # 고르지 않은 경우 함수 호출
    choose(wanna_choose, lastnum_idx+1,choosed)

choose(m,0,[])
