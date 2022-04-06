# 리스트(list)란?
# -순서가 있는 수정가능한 객체의 집합
# -대괄호([])로 작성되어지며, 리스트 내부의 값은 콤마(,)로 구분
# -추가,수정,삭제 가능

# 리스트 생성
li1 = []
li2 = [1,2,3]
li3 = ["a","b","c"]
li4 = [1,2,3,"a","b"]
li5 = [1,2,["a","b",3]]
print(li1)
print(len(li1))
print(li2)
print(len(li2))
print(li3)
print(len(li3))
print(li4)
print(len(li4))
print(li5)
print(len(li5))

#List 인덱싱
list1 = [2,3,4,5,6]
print(list1[0])
print(list1[-2])

list2 = [1,2,3,["a","b","c"]]

temp = list2[3]
print(temp)
print(list2[3][0])

#List 슬라이싱 -> 리스트명[start인덱스 : end인덱스]
list3 = [1,3,5,7,9]
print(list3[1:3])
print(list3[:2])
print(list3[3:])

list4 = [1,2,3]
list5 = [4,5,6]
print(list4+list5)

#리스트 값 수정하기
list6 = [1,3,5,7,9]
list6[1] = 8
print(list6)
list7 = [1,2,3,4,5,6]
list7[1:4] = [9]
print(list7)

#리스트 값 추가 append
list8 = [0,1,2,3,4]
list8.append(5)
list8.append(6)
print(list8)

#리스트 값 삽입 insert(인덱스번호, 값)
list9 = [0,1,2,3,4]
list9.insert(2,9)
print(list9)

#값 각제 delete
list10 = ['a','b','c','d']
del list10[3]
print(list10)

#특정 값 삭제 remove
list10.remove('a')
print(list10)

#리스트 순서 뒤집기
list11 = [100,12,4,7,2,9,5]
list11.reverse()
print(list11)

#리스트 정렬 sort(괄호안에 reverse가 true면 내림차순 false면 오름차순)
list12 = [100,12,53,26,37]
list12.sort(reverse=True)
print(list12)

#리스트 값 위치 반환
list13 = ['a','b','c','d']
print(list13.index('c'))

#튜플(tuple)이란?
# 순서가 있는 집합
# 소괄호()로 작성되어지며,튜플의 내부 값은 콤마(,)로 구분
# 추가,수정,삭제 불가능

#튜플 생성
t1 = (1,2,3)
t2 = (1,2,3,('a','b'))
print(t1)
print(len(t1))
print(t2)
print(len(t2))

#조건문에서 사용되는 in, not in
# in : 찾고자 하는 값(x)이 포함 되어 있으면 True
# not in : 찾고자 하는 값(x)이 포함되어 있지 안으면 True

name = "Hi, My name is Jonghyeon"
inputData = "Hi"

if inputData in name :
    print("포함되어있음")
else :
    print("포함되어있지않음")

fruit = ['수박','석류','사과','체리','포도']
inputData = input("검색할 문자를 입력하세요 : ")

if inputData in fruit :
    print(f"{inputData}는 {fruit.index(inputData)}번째 인덱스에 들어있습니다")
else :
    print(f"{inputData}는 문자열에 들어있지않습니다")