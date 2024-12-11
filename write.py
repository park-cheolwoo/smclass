import csv

with open("전국주차장정보표준데이터.csv", "r", encoding="ansi") as ff:
    reader = csv.reader(ff)
    with open("지번주소.txt", "w", encoding="utf-8") as f:
        for line in reader:
            if line[5].strip():  # 공백이 아닌 경우에만 입력
                print(line[5])
                f.write(line[5] + "\n")

print("작업 끝")
