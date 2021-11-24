num1=float(input("ENTER THE FIRST NUMBER: "))
num2=float(input("ENTER THE FIRST NUMBER: "))
op=input("ENTER THE OPERATOR[+ - * / %]: ")
result=0
if op=='+':
    result=num1+num2
elif op=='-':
    result=num1-num2
elif op=='*':
    result=num1*num2
elif op=='/':
    result=num1/num2
elif op=='%':
    result=num1%num2
else:
    print("INVALID OPERATOR")
print(num1,op,num2,'=',result)
