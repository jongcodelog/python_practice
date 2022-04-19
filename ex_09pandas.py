import pandas as pd

# Series 생성
population = pd.Series([9904312, 3445823, 2348524, 1312452])
print(population)

population = pd.Series([9904312, 3445823, 2348524, 1312452],
            index=['서울','부산','인천','대구'])
print(population)

# Series 데이터 확인
# index : 인덱스 확인
# values : 값 확인
# dtype : 데이터 타입 확인
print(population.index) 
print(population.values)
print(population.dtype)  
# Series 이름 지정
# Series에 이름 지정
population.name = '인구'
print(population)
# 인덱스에 이름지정
population.index.name = '도시'
print(population)

# Series 연산
p = population / 1000000
print(p)

# Series 인덱싱, 슬라이싱

# 인덱싱 - 가르키다
# index 번호(숫자)와 index값 둘다 활용 가능
print(population[0])
print(population['서울'])
print(population[3])
print(population['대구'])

# 슬라이싱 - [:]
# index 번호 - [포함 : 미포함]
print(population[1:3])
print('\n')
# index 문자열 -[포함 : 포함]
print(population['부산':'인천'])

# boolean 인덱싱
print(population >=2500000)
print(population[population >=2500000])

# 딕셔너리 객체로 Series 생성
# 딕셔너리는 key와 value로 구성
# key 값은 index
# value 값은 value
data = {  '서울':9483235,
       '부산':3353235,
       '인천':2183235,
       '대전':1283235,}
population2 = pd.Series(data)

print(population2)

# 2015년 도시별 인구
print(population.index)
print(population.values)

# 2010년 도시별 인구
print(population2.index)
print(population2.values)

pop = population - population2

print(pop)

# 2015년도와 2010년도의 인구 증가율(%) 계산

rs = (population - population2) / population2*100
print(rs)

# Series 데이터 갱신, 추가, 삭제
# 데이터 수정
rs['대구']=1.41
# 데이터삭제
del rs['대전']
# 데이터추가
rs['광주']=2.14
print(rs)