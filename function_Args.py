def Mul_Numbers(*args):
    print(type(args))
    result=1
    for Num in args:
     result *= Num
    return result
result=Mul_Numbers(1,2,3,4)
print(result)
