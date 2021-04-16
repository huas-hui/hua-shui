num1=int(input("请输入第一个数:"))
num2=int(input("请输入第二个数:"))
if  num1>num2:
    min=num2
else:
    min=num1
for i in range(1,min+1):
    if(num1 % i==0)and(num2%i==0):
        c=i
print('这两个数的最大公约数是:%d'%c)
        
