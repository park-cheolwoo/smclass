# a = "안녕하세요."
# print(a[1:])
# print(a[1:-1]) # 중요
# print(a[:-3])
# print(a[::-1]) # 중요

# lists = [1,2,3,4,5,6,7,8,9]
# print(lists[1:-1]) # 중요
# print(lists[:-1])
# print(lists[3:])
# print(lists[3:5])


# a = ""
# print(int(a))
# print("완료")


n_lists = [
    ["http://john", 100, 4.5, 1000],
    ["http://park", 80, 4.2, 800],
    ["http://lee", 90, 4.4, 2000],
    ["http://trump", 200, 4.7, 10],
    ["http://bill", 30, 4.3, 30],
]

print("기본 : ",n_lists)
# n_lists에서 1개(n_list) x대입
n_lists.sort(key=lambda x:x[0])
print("변경 : ",n_lists)