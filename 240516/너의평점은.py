# 졸업 조건
# 전공평점 >= 3.3
# 전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값
default = {
    "A+" : 4.5,
    "A0" : 4.0,
    "B+": 3.5,
    "B0" : 3.0,
    "C+": 2.5,
    "C0" : 2.0,
    "D+": 1.5,
    "D0" : 1.0,
    "F" : 0.0
}
score_list= []
while True:
    try:
        name, num, score = map(str, input().split())
        score_list.append({"name":name, "num":float(num), "score":score})
    except:
        break

filtered_list = [item for item in score_list if item['score'] != "P"]

length = len(filtered_list)

result = 0

sum_amount = sum([item['num'] for item in filtered_list])

for item in filtered_list:
    if item['score'] in default:
        result += item['num'] * default[item['score']]
    else:
        pass


print(result/sum_amount)
