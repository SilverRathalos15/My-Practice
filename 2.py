x = 5
y = 5
# hasil = x is 5 #untuk komparasi objek dgn literal, gunakan "=="
# variabel = (x + y - x) * x / y

# print(hasil, hex(id(x)))
# print(hasil, hex(id(y)))
# print('Python, youre the smartest languange amongs the other') #untuk objek dengan objek
#gunakan "is" dan "is not

# if variabel == x:
    # print('Nilai dari variabel dan x sama')

# a = True
# b = not a
# print('data a: ',a)
# print('data b: ',b)
# if a is False:
#     print('True')
# if a is True:
#     print('False')

# print('I think im fall in love with python')
# z = input('Did you felt the same thing? Yes or No ')

# if z == 'Yes':
#     print('Congratulations, you passed the test')
# if z == 'No':
#     print('Nice try, better luck next time')
# else:
#     print('Please answer within the answer requirement')

print('Pembuktian OR (V)')
print
a = True
b = True
c = a or b
print('-',a, 'V', b, '=', c)

a = True
b = False
c = a or b
print('-',a, 'V', b, '=', c)

a = False
b = True
c = a or b
print('-',a, 'V', b, '=', c)

a = False
b = False
c = a or b
print('-',a, 'V', b, '=', c)

print('\nPembuktian AND (^)')
print
a = True
b = True
c = a and b
print('-',a, '^', b, '=', c)

a = True
b = False
c = a and b
print('-',a, '^', b, '=', c)

a = False
b = True
c = a and b
print('-',a, '^', b, '=', c)

a = False
b = False
c = a and b
print('-',a, '^', b, '=', c)

#OR = salah satu saja true, maka true
#AND = salah satu saja false, maka false

a = True
b = False
c = False
d = a or b or c
print('-',a, 'V', b, 'V', c, '=', d)

a = True
b = False
c = False
d = a and b and c
print('-',a, '^', b, '^', c, '=', d)
    

institutTeknologiSepuluhNopember = 0.000000000000000000000000000000000000001
print(bool(institutTeknologiSepuluhNopember))