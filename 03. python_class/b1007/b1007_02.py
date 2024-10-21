numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
# 100 이상인 값만 출력하시오.
for s in numbers:
    if s >= 100:
        print(s)

numbers.sort()  # 순차정렬 - 낮은 수부터 출력
numbers.sort(reverse=True)  # 역순정렬 - 높은 수부터 출력


# 순서를 역순으로 출력
print(numbers)
numbers.reverse()
print(numbers)
