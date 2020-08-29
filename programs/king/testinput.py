bolEnd = False

while (not bolEnd):
    intA = input('输入第一个数：')
    strOper = input('输入操作符（+, -, *, /）: ')
    intB = input('输入第二个数：')
    if strOper == "+":
        print("ans: " + str(float(intA) + float(intB)))
    elif strOper == "-":
        print("ans: " + str(float(intA) - float(intB)))
    elif strOper == "*":
        print("ans: " + str(float(intA) * float(intB)))
    else:
        if (float(intB) == 0.0):
            print("除数不能为 0！")
        else:
            print("ans: " + str(float(intA) / float(intB)))
    strContinue = input('输入q退出或者回车继续：')
    if strContinue=="q":
        bolEnd = True