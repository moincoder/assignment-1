'''Print the following pattern 
1
22
333
4444
55555'''
a=1
while a<=5:
    i=1
    while i<=a:
        print(i, end='')
        i+=1
    print()
    a+=1