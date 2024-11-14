stu_title = ['번호','이름','국어','영어','수학','과학','합계','평균']
stu_datas = [
  [1,'홍길동',100,100,100,99],
  [2,'유관순',100,100,100,99],
 [3,'이순신',100,99,98,99],
 [4,'김구',80,100,90,99],
 [5,'김유신',80,100,90,99],
 ]

# append - 합계, 평균, 등수 추가 후 출력

stu_title.append("등수")
for s_t in stu_title:
  print("{}".format(s_t),end='\t') #(!)
print("\n")

print("-"*70)
for s in stu_datas:
  total = s[2]+s[3]+s[4]+s[5]
  avg = total/4
  s.append(total)
  s.append(avg)
  s.append("  ")
  print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}".format(s[0],s[1],s[2],s[3],s[4],
                                              s[5],s[6],s[7],s[8]))
