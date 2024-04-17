N = int(input())

for i in range(N):
    oxlist = list(input())
    score = 0
    sum_score = 0  # 새로운 OXlist 입력 받으면 점수합계 리셋
    for ox in oxlist:
        if ox == "O":
            score += 1  # "O" 연속되면 점수 1점씩 추가
            sum_score += score  # sum_score = sum_score+score #sum_score에 score 추가
        else:
            score = 0
    print(sum_score)
