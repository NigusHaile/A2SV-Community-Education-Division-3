if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    max_score = max(arr)
    scores = []
    
    for score in arr:
        if score != max_score:
            scores.append(score)
            
    arr = scores
    runner_up_score = max(arr)
    print(runner_up_score)
