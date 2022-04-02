# 조건문
# if 조건식 :
#     실행문장
#     실행문장

# if 조건식1 :
#     실행문장1
# elif 조건식2 :
#     실행문장2
# else :
#     실행문장3

# if문 구조
num1 = 25
num2 = 24

if num1>num2 :
    print("num1이 더 큽니다")
print("if문이 종료되었습니다.")

num1 = int(input("첫 번째 정수 입력>>"))
num2 = int(input("두 번째 정수 입력>>"))
if num1>num2 :
    print("첫 번째 정수가 더 큽니다")
elif num2>num1 :
    print("두 번째 정수가 더 큽니다")
else :
    print("두 수가 같습니다.")

score = int(input("점수 입력>>"))
if 100>=score>=90 :
    print(f"{score}점은 A학점입니다!")
elif 90>score>=80 :
    print(f"{score}점은 B학점입니다.")
elif 80>score>=70 :
    print(f"{score}점은 C학점입니다.")
elif 70>score>=60 :
    print(f"{score}점은 D학점입니다.")
else :
    print(f"{score}점은 F학점입니다")



print('='*50)
print(('='*17)+('-'*4)+' 자판기 '+('-'*4)+('='*17))
print('='*50)
print('== [1]콜라 == [2]사이다 == [3]물 =======[insert]==')
print('==---------==-----------==-------=======--------==')
print('==   600   ==    800    == 1000  =======[ 000원]==')
print('='*40+('-'*8)+'==')
print('='*50)
print('=='+'+'*46+'==')
print('=='+'+'*46+'==')
print('=='+'+'*46+'==')
print('=='+'+'*15+' '*16+'+'*15+'==')
print('=='+'+'*15+'     Hajong      '+'+'*15+'==')
print('=='+'+'*15+' '*16+'+'*15+'==')
print('=='+'+'*46+'==')
print('=='+'+'*46+'==')
print('='*50)
print('='*50)
print('  ==='+' '*40+'===  ')

coin = int(input("insert coin >>"))
menu = int(input("메뉴 선택 >>"))
change = 0

if menu == 1 :
    change = coin - 600
elif menu == 2 :
    change = coin - 800
elif menu == 3 :
    change = coin - 1000

if change < 0 :
    # 마지막에 잔돈 반환해주는 문장
    change = coin
    print("금액이 부족합니다.")

c_1000 = change//1000
c_500 = change%1000//500
c_100 = change%500//100

print(f"잔돈 >> 1000원 {c_1000}개 500원 {c_500}개 100원 {c_100}개")

