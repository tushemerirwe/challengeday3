mylist=[0,4,1,8,9,6,20]
missingnumbers = []
y = sorted(mylist)
print(y)
w = y[0]
print(w)
x = y[-1]
print(x)

for number in range(w,x+1):
    if number not in mylist:
        missingnumbers.append(number)

print(missingnumbers)        
