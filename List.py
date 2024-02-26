lst1 = []
lst2 = []

for i in range(5):
    lst1.append(input('Input string: '))

for s in lst1:
    if len(s) <= 2:
        lst2.append(s)
        
print(lst1)
print(lst2)
