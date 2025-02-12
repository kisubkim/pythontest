# 문자열 변수 선언
str_var = "This is my python code."
print(str_var)

# 인덱싱
print(str_var[11])  # p
print(str_var[-1])  # .
print(str_var[-5])  # c
print(str_var[11:17])   # python
print(str_var[11:-6])   # python
print(str_var[:10])     # This is my
print(str_var.isalpha())    # False --> space, period exist
print("Thisismypythoncode".isalpha())    # True --> no space, no period

num_var = "12"
print(num_var.isnumeric())  # True
print("12.3".isnumeric())   # False
print("123 ".isnumeric())   # False
print("12.3".isdecimal())   # False

# 문자열 더하기
num1 = 12
num2 = 34
print(num1 + num2)

snum1 = "12"
snum2 = "34"
print(snum1 + snum2)
print(snum1*3)


# 문자열 포맷팅
print("I have %d + %d apples." % (12, 34))
print("I have %s apples." % "twelve")
print(f"I have {snum1} and {snum2} apples.")

# .format 함수를 이용한 포맷팅
print("I have {} apples.".format(12))
print("I have {} and {} apples.".format(12, 34))
print("I have {1} and {0} apples.".format(12, 34))

# f-string
print(f"I have {12} apples.")
print(f"I have {12+34} apples.")
print(f"I have {num1} and {num2} apples.")
print(f"I have {num1} and {num2} apples. {num1} + {num2} = {num1+num2}")

num = input("숫자를 입력해 주세요: ")   # input 함수는 문자열로 입력받음
print(f"입력한 숫자는 {num}입니다.")    # num은 문자열

