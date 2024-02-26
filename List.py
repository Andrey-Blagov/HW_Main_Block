lst1 = []
lst2 = []
size_lst1 = int(input())

for i in range(len(size_lst1)):
    lst1.append(input('Input string: '))

for s in lst1:
    if len(s) <= 2:
        lst2.append(s)
        
print(lst1)
print(lst2)
