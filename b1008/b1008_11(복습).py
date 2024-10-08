a_str = "파이썬"
a = "-".join(a_str)
print(a)








ss = "파이썬 수업중 atype 문자열 atype,정수형 atype,실수형 atype,논리형 atype이 있습니다"

sss = ss.replace(" ","")
print (sss)
# idx = 0
# search = input("검색할 단어를 입력하세요. >> ")
# a_list = []
# # print(ss.find("atype",9))

# for i in range (ss.count(search)):
#   num = ss.find(search,idx) #0번부터 시작 - 8번
#   a_list.append(num)
#   print(num)
#   idx = num+1

# print(f"검색 개수 : {len(a_list)}, 위치값 : {a_list}")
# #검색 글자 개수
# idx = ss.count(i_str)
# print("개수 : ",idx)

# atype의 위치값을 모두 출력하시오.
# i_str = input("글자를 입력하세요.")
# idx = ss.find(i_str)

# for i in range(ss.count(i_str)):
#     print(idx)


# if i_str in ss:
#   print("있습니다")
# else:
#   print("없습니다.")

# 위치값 리턴
# idx = ss.find(i_str)
# print("위치값 : ",idx)
# idx = ss.index(i_str)  # 위치값 없을 때 에러
# print("위치값 : ",idx)


# # 1-20중 3의 배수만 리스트에 추가
# a_list = []
# for i in range(1, 21):
#     if i % 3 == 0:
#         a_list.append(i)

# # 리스트 내포[값 for문 조건]
# b_list = [i for i in range (1, 21) if i%3==0]
# print(b_list)


# aArr = [1,2,3,4,5]
# # a_list = [1,4,9,16,25]
# # 1줄 for문
# a_list = [i*2 for i in aArr]
# print(a_list)
