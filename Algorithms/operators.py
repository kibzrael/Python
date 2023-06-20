def multiply(num, factor):
    value = 0
    for i in range(factor):
        value+=num
    return value

def divide(num, factor):
    value = 0
    calc_num = num
    while calc_num>0:
        calc_num -= factor
        if(calc_num>0):
            value+=1
    return value

def modulus(num, factor):
    calc_num = 0
    while (num-calc_num)>factor:
        calc_num += factor
    value = num - calc_num
    return value

def power(num, factor):
    value = num
    for i in range(1, factor):
        calc_value = 0
        for j in range(num):
            calc_value+=value
        value = calc_value
    return value
         


print(f'Multiplication of 5 and three is {multiply(5,3)}')
print(f'Division of 9 by 2 is {divide(9,2)} remainder {modulus(9,2)}')
print(f'2 to the power of 3 is {power(2,3)}')


