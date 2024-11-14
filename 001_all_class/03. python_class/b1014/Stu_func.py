def stu_input(stuNo): # 함수 분리시 students도 매개변수로 넣어줘야함
    # while True:
    no = stuNo + 1
    print("no : ", no)
    name = input(f"{no}번째 학생 이름을 입력하세요.(0. 이전페이지 이동)")
    students.append({"no": no, "name": name})
    print(students)
    stuNo += 1
    return stuNo
