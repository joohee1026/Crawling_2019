for i in range(1,11):
    print("*"*i)

print("-"*30)

for i in range(1,11,2):
    print("*"*i)

print("-"*30)
for i in range(10,0,-1):
    print("*"*i)

# 3
for i in range(1, 11):
    for j in range(11, i, -1):
        print("*", end='')
    print("")

# 1
for i in range(1, 11):
    for j in range(0, i):
        print("*", end='')
    print("")

# 2
for i in range(1, 11, 2):
    for j in range(0, i):
        print("*", end='')
    print("")