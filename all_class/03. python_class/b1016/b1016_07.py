try:
  print("입력된 숫자 : ",int(input("숫자를 입력하세요. > ")))
except:
  pass

# try except : 프로그램 예외를 처리하는 명령어
# while True:
#   score = 100
#   print("[ 나눗셈 프로그램 ]")
#   nstr = input("숫자만 입력가능 >> ")


#   # 숫자가 아닌 것을 입력하거나 0을 입력하면 에러
#   try:
#     # print("숫자로 변환이 가능합니다.")
#     num = int(nstr)
#     print("입력된 숫자로 100을 나눔 : ",score/num)
#   except:
#     print("숫자로 변환이 불가합니다.")