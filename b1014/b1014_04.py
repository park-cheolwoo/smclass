def calc(a,b,op):
  if op == "+":
    return a+b
  elif op == "-":
    return a-b
  elif op == "*":
    return a*b
  elif op == "/":
    return a/b
  
num = int(input("숫자를 입력하세요."))
num2 = int(input("숫자를 입력하세요."))
op = input("+,-,*,/ 하나를 선택하세요.")

print("결과값 : ",calc(num,num2,op))