# Домашка 1 , задача 2: найдите сумму цифр трехзначного числа

#a = input("Ведите трехзначное число:")
#if ( a.isnumeric() and len(a)==3):
#    print(f"Сумма {a[0]} + {a[1]} + {a[2]} = {int(a[0])+int(a[1])+int(a[2])}")
#else :
#    print ("Некорректное число")

# Домашка 1 , задача 4:  Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

#a = input("Ведите обзее кол-во журавликов:")
# если Петя сделал Х журавликов. Сурежа сделал Х журавликов, а катя сделала 2Х+2Х журавликов. то S должно быть равно Х+Х+2Х+2Х ( S = 6X)   
#if ( a.isnumeric()):
#    S= int(a)
#    if ( S%6==0):
#        x = S/6
#        print (F"Петя сделал {x} журавлей, Сережа -  {x} , а Катя -  {4*x} ")
#    else: print ("Невозможное кол-во журавликов") 
#else : print ("Не число")

# Домашка 1 , задача 6:  Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет
#  с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета. 

#a = input("Ведите номер билета:")
#if ( a.isnumeric() and len(a) ==6):
#    if (int(a[0])+int(a[1])+int(a[2])) == (int(a[3])+int(a[4])+int(a[5])):
#        print ("Счастливый Билетик!")
#    else: print ("Не повезло") 
#else : print ("Неправильное число")

# Домашка 1 , задача 8: Требуется определить, можно ли от шоколадки размером n ×
#  m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника). 
#n = ""
#m = ""
#k = ""
#while not (n.isnumeric() and m.isnumeric() and k.isnumeric()):
#    n = input("Ведите кол-во долек в ширину :")
#    m = input("Ведите кол-во долек в длину :")
#    k = input("Ведите кол-во долек которое хотите отколоть :")
''''
else:
    k = int (k)   
    m = int (m) 
    n =  int (n) 
    if ((k%n==0 and (k/n) <=m) or (k%m == 0 and (k/m) <= n)):
        print ("Можно!") 
    else :  print ("Нельзя!")  

'''''
#Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в списке A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
'''
a = int(input("ВВедите число элементов списка:"))
list_1 = []
while a>0:
    list_1.append(int(input("ВВедите число:")))
    a-=1
a = int(input("ВВедите число, количество вхождений которого нужно узнать:")) 
print(list_1.count(a) )  
'''

#Задача 18: Требуется найти в списке A[1..N] самый близкий по величине элемент к заданному числу X.
#  Пользователь в первой строке вводит натуральное число N – количество элементов в списке. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
'''
a = int(input("ВВедите число элементов списка:"))
list_1 = []
while a>0:
    list_1.append(int(input("ВВедите число:")))
    a-=1
a = int(input("ВВедите число, близкое к которому нужно вывести:")) 
dic = {abs(a-element) : element for element in list_1}
print(dic[min(dic)])  
'''

#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
'''
n = int(input("ВВедите число элементов 1 списка :"))
m = int(input("ВВедите число элементов 2 списка :"))
list_n = []
list_m = []
while n>0:
    list_n.append(int(input("ВВедите число 1 списка:")))
    n-=1
while m>0:
    list_m.append(int(input("ВВедите число 2 списка:")))
    m-=1
Unique_n = set(list_n)
Unique_m = set(list_m)
r =  Unique_n.intersection(Unique_m)
print('список 1:'+ str(list_n) )  
print('список 2:'+ str(list_m) ) 
print('Результат:'+ str(sorted(r)))  
'''
#Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом,
#  у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
#Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
#В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
#Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
'''
n = int(input("ВВедите число высаженных кустов ( более 3):"))
list_n = []
while n>0:
    list_n.append(int(input("ВВедите число ягод на кусте:")))
    n-=1
#допустим. 1 заход. это когда модуль сдвигаетс яна 3  по часовой стрелке, если учитывать, что всегда начинает со второй
# и собьирает он минимум * 3 из выборки в куст. на котором стоим. куст + 1 . куст -1
# ок
sum = 0
for i in range(3,len(list_n),3):
    #print(i)
    new_n = list_n[i-3:i]
    #print (str(new_n))
    sum += min(new_n)*3
print('Результат ' + str(sum) )  
'''