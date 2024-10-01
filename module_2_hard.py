result = []
n = int (input ('ведите число от 3 до 20: '))
if n < 3 or n > 20:
    print('не верное число ')
else:
    for i in range(1,n):
        for y in range(1,n):
             if (i+y)%n == 0 and i!=y:
                 if i  not in result:
                      result.append(i)
                      result.append(y)

print(result)




