# condition.py

# 두 개의 값을 입력받습니다.
value1 = int(input("첫 번째 값을 입력하세요: "))
value2 = int(input("두 번째 값을 입력하세요: "))

# 값을 비교하고 결과를 출력합니다.
if value1 > value2:
    print("Win")
elif value1 < value2:
    print("Lose")
else:
    print("Draw")