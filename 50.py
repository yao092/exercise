a = set(['John','Mary','Tina','Fiona','Claire','Eva','Ben','Bill','Bert'])
b= set(['John','Mary','Fiona','Claire','Ben','Bill'])
c = set(['Mary','Fiona','Claire','Eva','Ben'])

print("英文與數學皆及格是",b & c)
print("數學不及格是",a - c)
print("英文及格但數學不及格是",b & (a - c))