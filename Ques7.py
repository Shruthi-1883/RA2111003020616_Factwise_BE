def max_Score(cardPoints, k):
    n = len(cardPoints)
    current_score = sum(cardPoints[:k])
    max_score = current_score
    for i in range(1, k + 1):
        current_score = current_score - cardPoints[k - i] + cardPoints[n - i]
        max_score = max(max_score, current_score) 
    return max_score

cardPoints_str = input("cardpoints: ").strip()

if cardPoints_str.startswith("[") and cardPoints_str.endswith("]"):
    cardPoints = list(map(int, cardPoints_str[1:-1].split(',')))
else:
    cardPoints = list(map(int, cardPoints_str.split(',')))
  
k = int(input("k: "))
result = max_Score(cardPoints, k)
print(result)

