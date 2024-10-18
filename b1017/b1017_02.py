subject = ["이름", "국어", "영어", "수학", "합계", "평균"]
students = []
s_title = ["name","kor","eng","math","total","avg"]
k_title = ["이름", "국어", "영어", "수학", "합계", "평균"]

### 함수 선언 ###
def stuScore_update(choice,k_title,s_title,s):
    print(f"현재 {k_title}점수 : {s_title}")
    s[s_title] = int(input(f"수정할 {s[choice]}점수를 입력하세요."))


while True:
    print("1. 학생성적 입력")
    print("2. 학생성적 출력")
    print("3. 학생성적 수정")
    choice = int(input("원하는 번호를 입력하세요. >> "))
    if choice == 1:
        name = input("이름을 입력하세요. >> ")
        score = []  # 국어, 영어, 수학
        sum = 0
        for i in range(len(subject) - 3):
            num1 = int(input(f"{subject[i+1]}점수를 입력하세요. >> "))
            score.append(num1)
            sum += num1
        avg = sum / len(score)
        s = {
            "name": name,
            "kor": score[0],
            "eng": score[1],
            "math": score[2],
            "total": sum,
            "avg": avg,
        }
        students.append(s)
        print(students)
    elif choice == 3:
        flag = 0
        name = input("이름을 입력하세요.")
        for s in students:
            if name == s["name"]:
                flag = 1
                print(f"{name} 학생을 찾았습니다.")
                print("1. 국어 2. 영어 3. 수학 0. 이전화면이동")
                choice = int(input("원하는 번호를 선택하세요."))
                if choice == 1:
                    stuScore_update(choice,subject[choice],"kor",s)
                if choice == 2:
                    stuScore_update(choice, subject[choice], "eng", s)
                if choice == 3:
                    stuScore_update(choice, subject[choice], "math", s)
                if choice == 0:
                    break
                s["total"] = s["kor"] + s["eng"] + s["math"]
                s["avg"] = s["total"] / 3
                print(f"{name} 학생 성적이 수정되었습니다.")
        if flag == 0:
            print(f"{name} 학생을 찾지 못했습니다.")
