# a_list = [1,2,3]
# ###추가###
# print(a_list)
# a_list.append(4) #리스트에 추가 : append - 제일 뒤쪽에 추가, insert - 원하는 위치 추가
# print(a_list)
# a_list.append(10)
# print(a_list)
# a_list.insert(0,50)
# print(a_list)
# a_list.insert(3,20)
# print(a_list)


# ###삭제 del - index위치에 데이터 삭제, remove - 데이터 값으로 삭제###
# del a_list[0] #형식 유의
# print(a_list)
# del a_list[2]
# print(a_list)

# a_list.remove(4)
# print(a_list)
# a_list.remove(1)
# print(a_list)

stu = [1,'홍길동',100,100,100,99]
### 합계, 평균을 추가 ###
stu.append(stu[2]+stu[3]+stu[4]+stu[5])
stu.append((stu[2]+stu[3]+stu[4]+stu[5])/4)
print(stu)




# 자바스크립트 vs 파이썬
# 배열 뒤에 추가 : push | append
# 특정 순서에 추가 : index (n) 'm' | insert(n,m)
# 특정 순서 삭제 :  splice(n,1) | del list[n]
# 특정 데이터 삭제 : | remove
# pop : 맨 뒤에서부터 삭제