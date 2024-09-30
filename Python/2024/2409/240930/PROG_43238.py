def solution(n, times):
    max_time = max(times) * n
    min_time = 1
    answer = max_time
    while min_time <= max_time:
        mid = (min_time + max_time) // 2
        
        result = 0
        for time in times:
            result += mid // time
        
        if result >= n:
            answer = mid
            max_time = mid - 1
        else:
            min_time = mid + 1
    return answer