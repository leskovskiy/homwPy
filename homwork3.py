##Задайте список из нескольких чисел. Напишите 
# программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции

A = [2, 3, 5, 9, 3]
my_sum = 0
for i in range(len(A)) :
    if i % 2 != 0 :
        my_sum = my_sum + A[i]
print('Task1 ')
print(A)
print(my_sum)

##Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

my_list = [2, 3, 4, 5, 6]
my_mult = []

for i in range(len(my_list)) :
    if len(my_list) % 2 != 0:
        len(my_list)//2 + 1
    else:
        len(my_list)//2
    my_mult = my_list[i] * my_list[len(my_list) - i - 1]
print('Task2 ')    
print(my_list)
print(my_mult)


#Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.

my_list = [1.1, 1.2, 3.1, 5, 10.01]
new_lst = []
for i in my_list :
    if i % 1 != 0 :
        i = round(i % 1,2)
        new_lst.append(i)
print('Task3 ')
print(max(new_lst) - min(new_lst))


#Напишите программу, которая 
# будет преобразовывать десятичное число в двоичное.

x = int(input('Введите число : '))
d = 0
elem = 2
d = x % elem
res = str(d)
x = x // 2
while x > 0 :
    d = x % elem
    res = str(d) + res
    x = x // elem
print('Task4 ')
print(res)