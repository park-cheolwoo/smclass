students = [
    [1, "홍길동", 100, 90, 99],
    [2, "유관순", 100, 100, 99],
    [3, "이순신", 100, 100, 99],
    [4, "강감찬", 100, 90, 99],
    [5, "김구", 90, 90, 99],
]

# 합계, 평균 추가
for s in students:
    sum = s[2] + s[3] + s[4]
    avg = sum / 3
    s.append(sum)
    s.append(avg)
    s.append(0)


# 출력
s_title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균", "등수"]

# 상단 출력
for s in s_title:
    print(s, end="\t")
print()
print("-" * 60)

# 학생 성적 출력
for s in students:
    print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")
