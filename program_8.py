list1 = [10,20,25,30,35]
list2 = [40,45,60,75,90]
flist =[]
for a in list1:
    if a%2!=0:
        flist.append(a)
for a in list2:
    if a%2==0:
        flist.append(a)
print(flist)