N = int(input())
scoreList = list(map(int, input().split()))
maxScore = max(scoreList)
newScoreList = []
for i in range(N):
    newScoreList.append(scoreList[i]/maxScore*100)
print(sum(newScoreList) / N)
