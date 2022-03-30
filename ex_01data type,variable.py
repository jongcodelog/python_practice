num = 3
print(num)

name = "하종현"
print(name)

# 변수 사용
a = 10
b = 15
c,d = 10,15
print(a,b,c,d)

# 변수에 문자열 넣기
str1 = "python"
str2 = "python"
str3 = str4 = "python"
print(str1,str2,str3,str4)

# 문자열 사용방법
# '문자열' vs "문자열"
# 문자열 안에 '표현하고 싶을때는 "" 사용
# 문자열 안에 "표현하고 싶을때는 '' 사용

s1 = 'she\'s gone'
print(s1)

s2 = "she's gone"
print(s2)

# \n 줄바꿈
# \t 탭
# \\ 문자 "\"
# \' 단일 인용부호(')
# \" 이중 인용부호(")

# 인덱싱과 슬라이싱

# 문자열 인덱싱
my = "My name is jonghyeon"
print(my[0])
print(my[4])
print(my[11])

print(my[3]+my[4]+my[5]+my[6])

# 문자열 슬라이싱

mys = "My name is jonghyeon"
print(mys[0:2])
print(mys[0:7])
print(mys[:7])
print(mys[11:])

day = "2022년 3월 30일의 날씨는 흐림."
print("날짜 :"+day[:11])
print("날씨 :"+day[18:20])

# 문자열 포매팅

# 문자열 내 값 삽입 방법
# %s = 문자열
# %c = 문자1개
# %d = 정수
# %f = 실수
# %% = (문자 '%'자체)

# % 기호 포매팅 -> %d를 활용한 정수 대입
month = 3
day = 30
today = "오늘은 %d월 %d일 입니다."%(month, day)
print(today)

# format함수 포매팅
month = 3
day = 30
today = "오늘은 {}월 {}일 입니다.".format(month, day)
print(today)

# f문자열 포매팅
month = 3
day = 30
today = f"오늘은 {month}월 {day}일 입니다."
print(today)

x = 100
y = 200
sum = x+y
plus = f"{x}와 {y}의 합은 {sum}이다."
print(plus)

# 문자열 관련 함수

name = "My name is Hajonghyeon"
# 문자열에 포함된 문자 개수 세기
print(name.count("a"))
print(name.count("Hajonghyeon"))

# 문자 위치 알려주기
print(name.index("i"))

# 대소문자 변환
print(name.upper())
print(name.lower())

# 문자열 바꾸기
print(name.replace("Hajonghyeon", "jonghyeon"))

# 문자열 자르기
print(name.split(" "))