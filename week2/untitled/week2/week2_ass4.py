players = ["황의조", "황희찬", "구자철", "이재성", "기성용"]

for i in players:
    print(i)

print('-'*30)

num = input("OUT 시킬 선수 번호: ")
name = input("IN 할 선수 이름: ")
print('-'*30)
#players[int(num)] = name

del players[int(num)]
players.append(name)

print("교체 결과: ")
for i in players:
    print(i)
