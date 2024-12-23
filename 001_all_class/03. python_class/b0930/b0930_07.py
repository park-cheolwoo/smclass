stu_data = ['홍길동',100,100,100,99]
stu_title = ['번호','이름','국어','영어','수학','과학','합계','평균']
stu_datas = [
  [1,'홍길동',100,100,100,99],
  [2,'유관순',100,100,100,99],
 [3,'이순신',100,99,98,99],
 [4,'김구',80,100,90,99],
 [5,'김유신',80,100,90,99],
 ]

# for 문 사용하여 출력

print("                 [ 학생 성적 프로그램 ]")
# print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(stu_title[0],stu_title[1],stu_title[2],stu_title[3],
#                                                 stu_title[4],stu_title[5],stu_title[6],stu_title[7]))
for s_t in stu_title:
  print("{}".format(s_t),end='\t')
print("\n")
print("-"*60)
for s in stu_datas: # s >> stu_datas(객체) 내의 한 줄(배열)
  print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(s[0],s[1],s[2],s[3],
                                                s[4],s[5],
                                                s[2]+s[3]+s[4]+s[5], 
                                                (s[2]+s[3]+s[4]+s[5])/4))


