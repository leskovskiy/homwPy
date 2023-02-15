#Задайте натуральное число N. Напишите программу, которая составит 
# список простых множителей числа N.

n = int(input())
my_list = []
for i in range(1, n+1):
    if n % i == 0 :
        my_list.append(i)
print(my_list)


##Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся
#  элементов исходной последовательности.


my_list = [4, 5, 6, 7, 7, 13 ]
new_my_list = []
for i in range(len(my_list)):
    if my_list[i] not in new_my_list:
        new_my_list.append(my_list[i])
print(new_my_list)