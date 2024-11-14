# a = [1,2,3]
# b = [4,5,6,7]
# print(a+b)

a = ['1만','3,450','1.7만','500','1,000']
b = []
for i in a:
  if "만" in i : i = i[:-1]
  elif "," in i : i = i.replace(",","")
  i = float(i)
  b.append(i)
print(a)