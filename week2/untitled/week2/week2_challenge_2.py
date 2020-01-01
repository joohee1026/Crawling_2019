data = ["조회수: 1,500", "조회수: 1,002", "조회수: 300", "조회수: 251",
        "조회수: 13,432", "조회수: 998"]
sum = 0

i = 0
for i in data:
    print(i)

i = 0
for i in range(i,(len(data))):
    print(data[i].replace("조회수: ","").replace(",",""))

i = 0
for i in range(i,(len(data))):
    k = data[i].replace("조회수: ","").replace(",","")
    print(k)
    sum += int(k)

print("총 합:",sum)

## 모범답안
data = ["조회수: 1,500", "조회수: 1,002", "조회수: 300", "조회수: 251",
        "조회수: 13,432", "조회수: 998"]
sum = 0

for d in data:
    # 슬라이싱을 이용해서 /조회수: /를 잘라줍니다.
    d = d[5:]
    # ,를 빈칸으로 바꿔줍니다.
    d = d.replace(",", "")

    # d는 문자이므로 연산을 위해서 숫자로 바꿔줍니다.
    d = int(d)

    # sum에 d(조회수)를 저장해서 다시 sum에 저장합니다.
    # 이 방법을 사용하면 데이터를 누적해서 저장할 수 있습니다.
    sum = sum + d
    print(d)