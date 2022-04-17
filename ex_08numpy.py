# numpy 라이브러리를  가져와서 np라고 부르겠다.
import numpy as np
from regex import F

# 1차원 배열(array) 만들기
list1 = [1,2,3,4,5]

# numpy에 있는 array라는 자료형
arr = np.array(list1)
print(arr)

# 2차원 배열(array) 만들기
list2 = [[1,2,3],[4,5,6]]
arr2 = np.array(list2)
print(arr2)

# 배열확인
# shape : 배열의크기
# size : 총 요소 개수 확인
# ndim : 배열의 차원 확인
print(arr2.shape)
print(arr2.size)
print(arr2.ndim)

# 배열의 타입 확인
# dtype : 타입확인
print(arr2.dtype)

# 3차원 배열 만들고 확인하기
list3 = ([[[1,2],[3,4]],[[5,6],[7,8]]])
arr3 = np.array(list3)
print(arr3)

print(arr3.shape)
print(arr3.size)
print(arr3.ndim)

# array 만들기
# 특정 값으로 배열 생성

# 0으로만 이루어진 배열 생성
# zeros((행,열))
print(np.zeros((3,4)))

# 1로 이루어진 배열 생성
print(np.ones((2,5)))

# 원하는 값으로 이루어진 배열 생성
print(np.full((3,3), 4))

# 범위 배열 생성하기
list = []
for i in range(1,51) :
    list.append(i)
print(list)

# 리스트를 배열로 바꾸기
print(np.array(list))

# 범위 배열 만드느 함수 
print(np.arange(1,51))

# 랜덤 값 생성하기
# 0~1 사이 값 생성
print(np.random.rand(2,3))

# 랜덤 정수 생성하기
# (시작,n-1) 사이의 랜덤한 정수 1개 생성
print(np.random.randint(2,10))

# 여러 정수 생성
print(np.random.randint(2,10,size=(2,3)))

# array연산

list1 = [1,2,3,4]
list2 = [5,6,7,8]

arr1 = np.array(list1)
arr2 = np.array(list2)

print(arr1+arr2)

# 인덱싱
arr = np.array([[1,2,3],[4,5,6]])
print(arr[0][1])

# 슬라이싱
arr = np.arange(10)
print(arr[3:7])

# 2차원 배열
# 배열의 크기 재지정
arr = np.arange(50).reshape(5,10)
print(arr)

# 2차원 배열 슬라이싱
# [행범위,열범위]

print(arr[ :2, : ])


# np.loadtxt('파일명,확장자')
# delimiter 구분기호
data = np.loadtxt('height_weight.txt', delimiter=',')
print(data)

height = data[0]
weight = data[1]
print(height)
print(weight)

height_m = height*0.01
print(height_m)

bmi = weight/(height_m*height_m)
print(bmi)

#boolean 인덱싱
name = np.array(['종현','정민','민지'])
bol = np.array([True,False,False])
print(name[bol])

# 다양한 함수들

# 1~10까지 담긴 1차원 배열 생성
arr = np.arange(1,11)

# 생성한 배열을 (2,5)크기로 
arr = np.arange(1,11).reshape(2,5)
print(arr)

# np.sum()
# 종합, 요소 더하기
print(np.sum(arr))
print(np.sum(arr, axis=0))
print(np.sum(arr, axis=1))

# np.mean() 평균
print(np.mean(arr))
print(np.mean(arr, axis=0))
print(np.mean(arr, axis=1))

# np.abs() 절대값
arr = np.array([1,-2,3,-4,5])
print(np.abs(arr))
