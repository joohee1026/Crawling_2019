print("일반계산기 프로그램입니다!")
num1 = input("계산할 첫번째 값을 입력해주세요 : ")
num2 = input("계산할 두번째 값을 입력해주세요 : ")

print("두 개의 값 :", num1, "와", num2)
num1 = int(num1)
num2 = int(num2)

print("더하기 값 (a + b) : ", num1 + num2)
print("빼기 값 (a - b) : ", num1 - num2)
print("곱하기 값 (a * b) : ", num1 * num2)
print("정수 나누기 값 (a // b) : ", num1 // num2)
print("실수 나누기 값 (a / b) : ", num1 / num2)
print("나머지 값 (a % b) : ", num1 % num2)
