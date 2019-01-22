#!/usr/bin/env python3
list = []
while(True):

    print("---------------Calculator---------------")

    a = int(input("Enter first operand : "))
    list.append(a)
    b = int(input("Enter second operand : "))
    o = input("Enter operator : ")
    list.append(o)
    list.append(b)
    list.append('=')

    if(o == '+'):
        print(a+b)
        list.append(a+b)

    elif(o == '-'):
        print(a-b)
        list.append(a-b)

    elif(o == '*'):
        print(a*b)
        list.append(a*b)

    elif(o == '/'):
        print(a/b)
        list.append(a/b)

    elif(o == '%'):
        print(a%b)
        list.append(a%b)

    else:
        print("ERROR!!! NO OPERATOR FOUND!!! RESTART")
        continue

    k = input("More calculation??(y/n)")
    if(k == 'n' or k == 'N'):
        break


print("\nAll calculations performed this session : \n")
for _ in range(len(list)):
    print(list[_],end=' ')
    if(_!=0 and _%5==4):
	    print("")
