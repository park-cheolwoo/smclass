# 리스트 함수
a_list = [1, 2, 3, 4, 3, 5, 60, 3, 70, 3]
# 리스트 함수 - 추가
# a_list.append(200) #뒤에 값 추가
# a_list.insert(0,100) #index 위치에 해당값 지정

# 리스트 함수 - 삭제
a_list.pop(2)  # 해당 index 위치 삭제
# del(a_list[3]) #해당위치 리스트 삭제
# a_list.remove(3) #입력된 값을 찾아 리스트 삭제
a_list.clear()  # 전체 삭제


# print(a_list.count(3)) #입력된 값의 존재 개수
# print(len(a_list)) #리스트 개수 - 5
print(a_list)

# 리스트 삭제
# a_list = [1, 2, 3, 4, 5]

# a_list = [] #전체삭제(공간은 있음)
# a_list = None # 전체삭제 - None(공간은 있음)
# del(a_list) # a_list 자체를 삭제

# del 명령어 사용
# del a_list[0] #[2,3,4,5]
# a_list[1:3] = [] #2개 삭제시 - [2,5]
# print(a_list)

# 리스트 수정 방법
# a_list = [1,2,3,4,5,6,7]
# a_list[3]=50 #1개 변경시
# a_list[1:2] = [20,30] #2개 변경시
# a_list[4] = [10,20] #리스트 안에 리스트로 변경
# print(a_list)


# 리스트 출력 방법
# a_list = [1,2,3,4,5]
# b_list = [50,100]
# print(a_list[0:3]) #1,2,3
# print(a_list[2:4]) #3,4
# print(a_list[:3]) #1,2,3
# print(a_list[3:]) #4,5
# print(a_list+b_list) #1,2,3,4,5,50,100
# print(b_list*3) # 50,100,50,100,50,100
# print(a_list[::2]) #1,3,5
# print(a_list[::-2]) #5,3,1
# print(a_list[::-1]) #5,4,3,2,1


# a_list = [1,2,3,4,5]
# b_list = a_list #얕은 복사
# a_list[0] = 100 # a_list를 변경하면 b_list도 같이 변경됨
# print(a_list)
# print(b_list)

# 리스트를 역순으로 복사
# b_list = a_list[::-1]
# print(a_list)
# print(b_list)
# a_list[0] = 100
# print(a_list)
# print(b_list)


# b_list = a_list[:] #깊은 복사
# a_list[0] = 100 #a_list를 변경해도 b_list가 변경되지 않음
# print(a_list)
# print(b_list)


# 순차적 출력
# for i in a_list:
#   print(i)

# 역순 출력
# for i in range(1,len(a_list)+1):
#   print(a_list[-i])

# for i in range(len(a_list)):
#   print(a_list[-(i+1)])


# a_list = [1,2,3.0,"안녕",True,False] #문자열, 숫자-정수형, 숫자-실수형, 논리형
# print(a_list[0])
# print(a_list[3])
# print(a_list[-1])


# a_list = []
# total = 0
# #1~100 들어가있는 리스트를 출력하시오.
# for a in range(100):
#   a_list.append(a+1)
#   total += (a+1)
# print("합계 : ",total)


# a,b,c,d,e,f,g = 0,0,0,0,0,0,0
# total = 0

# #변수 a,b,c,d,e,f,g의 변수에 숫자를 입력받아 합계를 출력하시오.

# a=int(input("숫자를 입력하세요."))
# b=int(input("숫자를 입력하세요."))
# c=int(input("숫자를 입력하세요."))
# d=int(input("숫자를 입력하세요."))
# e=int(input("숫자를 입력하세요."))
# f=int(input("숫자를 입력하세요."))
# g=int(input("숫자를 입력하세요."))
# total = a+b+c+d+e+f+g
# print(total)

# a_list = []
# total = 0

# for i in range(10):
#     j = int(input(f"{i+1}번째 숫자를 입력하세요."))
#     a_list.append(j)
#     total += j

# for idx, a in enumerate(a_list):
#   a=int(input(f"{idx+1}번째 숫자를 입력하세요."))
#   total += a

# print("합계 : ",total)
