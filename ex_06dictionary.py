# 딕셔너리
# key값은 변할 수 없는 값
# value값은 변할 수 있는 값
# 딕셔너리는 key:value 맵핑되어져 있는 자료구조

# 딕셔너리 선언
# 인물정보를 담아보기
dict1 = {"name":"하종현","birth":"0905","phone":"010-1234-5678"}
print(dict1)
#딕셔너리 새로운 데이터 추가
dict1["blood"] = "O형"
print(dict1)

# 딕셔너리 key를 통해 데이터접근
print(dict1["birth"])

#딕셔너리 값 수정
dict1["birth"] = "19980905"
print(dict1)

# 혈액형 정보 삭제
del dict1["blood"]
print(dict1)

# 모든 정보 삭제
dict1.clear()
print(dict1)

# 딕셔너리 관련 함수
# keys() : 키값들 확인 함수
# values() : 벨류값들 확인 함수
# items() : 키와 벨류 확인 함수