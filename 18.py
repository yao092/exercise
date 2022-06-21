a = 0
b = input("輸入五張牌:").split()

for i in range(len(b)):
  if b[i] == "A":
    b[i] = 1 
  if b[i] == "J":
    b[i] = 11 
  if b[i] == "Q":
    b[i] = 12
  if b[i] == "K":
    b[i] = 13
for i in range(len(b)):
    a+=int(b[i])
print(a)