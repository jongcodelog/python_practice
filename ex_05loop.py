#반복문 종류는 while문, for문이 있다.
#while문은 반복 횟수가 명확하지 않을 때
#for문은 반복 횟수가 명확할 때

cw = int(input("현재 몸무게 :"))
gw = int(input("목표 몸무게 :"))
week = 1
while True :
    lw = int(input(f"{week}주차 감량 몸무게 :"))
    cw = cw-lw
    week = week+1

    if cw<=gw :
        break
print(f"{cw}kg 달성 축하합니다!")

list_food = ["햄버거","치킨","짜장면"]
for food in list_food :
    print(food)

tuple_chick = ("양념치킨","간장치킨","후라이드")
for food in tuple_chick :
    print(food)

text = "안녕하세요"
for t in text :
    print(t)

number = 1
score_list = [90,40,55,67,80]
for sc in score_list :
    if sc >= 60 :
        print(f"{number}학생은 합격입니다.")
    else :
        print(f"{number}학생은 불합격입니다.")
    number += 1

# range() 함수 사용
# range(시작할숫자,종료할숫자,증가량)
# range(1,10,1) -> 1부터9까지 1씩증가
# range(1,100,3) -> 1부터 99까지 3씩증가
# range(10,1,-1) -> 10부터 2까지 1씩감소
# range(기본값0,종료할숫자,기본값1)
# range(3,10) -> 3부터9까지 1씩증가
# range(10) -> 0부터9까지 1씩증가
