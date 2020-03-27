# 레퍼런스 카운트와 가비지 컬렉션
# 가비지 컬렉션 : 객체를 아무도 참조하지 않는 상황에 소멸대상이 됨 (rc=0)
r = [1, 2, 3] # r이라는 이름으로 리스트를 참조
r = 'simple' # [1, 2, 3]

r1 = [1, 2, 3] # [1, 2, 3] rc=1
r2 = r1 # rc=2
r1 = 'simple' # rc=1
r2 = 'happy' # rc=0, 따라서 [1, 2, 3]리스트는 가비지 컬렉션 대상