# 함수란? 
# 하나의 특별한 목적의 작업을 수행하기 위해 독립적으로 설계된 코드의 집합

# 함수를 사용하는 이유
# 반복적인 프로그래밍을 피할 수 있다.
# 모듈화로 인해 전체적인 코드의 가독성이 좋아진다.
# 프로그램에 문제가 발생하거나 기능의 변경이 필요할 때에도 손쉽게 유지보수가 가능.

# 파이썬 함수 정의 방법
def 함수명(매개변수):
    실행문장1
    실행문장2
    return 반환결과

# 더하기 기능하는 함수 정의
def number_add(num1,num2) :
    result = num1+num2
    return result
result = number_add(9,5)
print(result)

# 두 수를 입력 받아서 뺀 결과를 return하는 함수를 정의
def number_sub(n1,n2) :
    return n1-n2
num1 = int(input("첫 번째 정수 입력>>"))
num2 = int(input("두 번째 정수 입력>>"))

result = number_sub(num1,num2)
print(result)

# 특정문자를 찾아서 다른걸로 변경하는 함수 replace
print("안녕하세요~".replace("~","!"))

# 입력받은 문자열에서 ㅋ을 제거해주는 함수 정의
def s_replace(str1):
    return str1.replace("ㅋ","").strip()
s = input("문자열 입력>>")
result = s_replace(s)
print(result)

def cal(num1, num2, op) :
    if op == "-":
        result = num1-num2
    elif op == "+":
        result = num1+num2
    return result
num1 = int(input("첫 번째 정수 입력>>"))
num2 = int(input("두 번째 정수 입력>>"))
op = input("연산자 입력(-,+)")
result = cal(num1, num2, op)
print(f"결과: {result}")

# 가변 매개변수 
# 함수 호출 시 몇개의 인수가 전달될지 알 수 없을때 사용
# 사용자가 직접 매개변수의 개수를 정할 수 있도록 선언
# 키워드 *

# 제곱하는 함수 정의하기
# 지수연산자 **
def power_of_N(num,power):
    return num**power
print(power_of_N(2,3))
