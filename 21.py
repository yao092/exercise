x = [["123","Tom DTGD"],["456","Cat CSIE"],["789","Nana ASIE"],["321","Lim DBA"],["654","Won FDD"]]
y = input("輸入查詢學號 : ")

for z in range(len(x)):
    if y == x[z][0]:
        print("學生資料為:",y,x[z][1])