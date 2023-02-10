#Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.

x =int(input('введите чилов : '))
my_summ = 0 
while x > 0 :
    d = x % 10 
    my_summ = my_summ + d 
    x = x // 10
print(my_summ)



##Напишите программу, которая принимает на вход число 
# N и выдает набор произведений чисел от 1 до N.

n =int(input('введите чилов : '))
my_mult = []
f = 1 
for i in range(1,n+1) :
    f = f * i 
    my_mult.append(f)
print(my_mult)

#Задайте список из N элементов, заполненных числами из 
# промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.

n = int(input('Введите число: '))
N = []
my_mult = 1 
for i in range(-n,n + 1):
    N.append(i)
    for i in range(0,len(N)):
        my_mult = my_mult * i
print(N)
print('Произведение элементов = ', my_mult)

#Реализуйте алгоритм перемешивания списка.
import random

D = ['dog', 'cat', 'rabbit', 'crocodile']
print(D)
random.shuffle(D)
print(D)