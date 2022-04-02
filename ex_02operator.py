# 연산자 종류
# 산술연산자 = + - * / // %
# 지수연산자 = **
# 대입연산자 = = += -= *= /= //= %=
# 관계연산자 = > >= < <= == !=
# 논리연산자 not and or
# 멤버연산자 in notin
# 삼항연산자 a if 조건식 else b

num1 = 10
num2 = 4

print(num1/num2)
print(num1//num2)

# 문자열끼리의 산술 연산은 더하기만 가능하다

str1 = "안녕"
str2 = "하세요"
print(str1+str2)

# 문자열과 숫자의 더하기연산은 불가능하다
str3 = "10"
str4 = "7"
print(str3+str4)

# 문자열과 숫자는 곱하기연산은 가능하다
num3 = 5
str5 = "하이"
print(str5*num3)

# 키보드로 입력받는 input() 사용법
num = int(input("정수를 입력하세요 : "))
print(int(num)+1)

num4 = int(input("첫 번째 정수 입력 :"))
num5 = int(input("두 번째 정수 입력 :"))
print("더하기 : "+ str(num4+num5))
print("빼기 : "+ str(num4-num5))
print("곱하기 : "+ str(num4*num5))
print("나누기 : "+ str(num4/num5))

# 반올림 함수
round(123.4567, 3)

# 문자길이 확인함수
str6 = "안녕하세요"
print(len(str6))

# 초입력해서 시,분,초 구하기
time = int(input("초입력 : "))
hour = time//3600
minute = time%3600//60
second = time%60
print(f"{hour}시간 {minute}분 {second}초")

# 지수연산자(**)
num = int(input("정수 입력 :"))
power = int(input("지수 입력 :"))
print(str(num)+"의"+str(power)+"승은"+str(num**power)+"이다.")

# 대입연산자
# 치환
num1 = 10
num2 = 20

temp = num1
num1 = num2
num2 = temp
print(num1, num2)

# python에서만 가능한 치환방법
num3 = 20
num4 = 30

num3, num4 = num4, num3
print(num3, num4)

# 삼항연산자
score = 90
"합격" if score >= 70 else "불합격"

a = int(input("정수입력 :"))
b = int(input("정수입력 :"))
print(f"a: {a}" if a>b else f"b: {b}")

a = int(input("정수 입력 :"))
print(f"{a}은 짝수입니다" if a%2==0 else f"{a}은 홀수입니다.")
