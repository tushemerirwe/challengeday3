list=[0,4,1,8,9,6,20]
missingnumbers = []
y = sorted(list)
print(y)
w = y[0]
print(w)
x = y[-1]
print(x)
for number in range(w,x+1):
    if number not in list:
        missingnumbers.append(number)
print(missingnumbers)        
