def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p1_len = len(p1)
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p2_len = len(p2)
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    p3_len = len(p3)
    
    p1_score = 0
    p2_score = 0
    p3_score = 0
    
    for i in range(len(answers)):
        if (answers[i] == p1[i%p1_len]):
            p1_score += 1
        if (answers[i] == p2[i%p2_len]):
            p2_score += 1
        if (answers[i] == p3[i%p3_len]):
            p3_score += 1
    
    max_score = max(p1_score, p2_score, p3_score)
    # scores = [(1, p1_score), (2, p2_score), (3, p3_score)]
    scores = [p1_score, p2_score, p3_score]
    
    result = [x[0] for x in list(enumerate(scores, start=1)) if x[1] == max_score]
    result.sort()
    
    return result