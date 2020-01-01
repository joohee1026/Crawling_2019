yymmdd = "881120-1068234"
print(yymmdd[:6])
print(yymmdd[7:])

a = "a:b:c:d"
print(a.replace(":","#"))

sum = 0
score = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
for i in score:
    sum += i
print(sum/len(score))

for i in range(0,9):
    print(" "*i,end='')
    print("*"*(9-i))

for i in range(0,9):
    print(" "*i+"*"*(9-i))