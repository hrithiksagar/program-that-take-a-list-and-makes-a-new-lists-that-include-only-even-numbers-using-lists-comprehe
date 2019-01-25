l=[]
s=int(input("input the size of list"))
for i in range(s):
    x=int(input("enter list items"))
    l.append(x)
print("list that you entered is: ",l)
list2=[i for i in  l if i%2==0]
print("new list that include only even numbers is",list2)