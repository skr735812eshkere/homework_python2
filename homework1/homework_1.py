import array
from runpy import run_path

import numpy as np
import sys

from numpy.ma.core import arange

#Типы данных Python
# x = 1
# print(type(x))
# print(sys.getsizeof(x))
#
# x = 'hello'
# print(type(x))
#
# x = True
# print(type(x))

# l1 = list([])
# print(sys.getsizeof(l1))
#
# l2 = list([1, 2, 3])
# print(sys.getsizeof(l2))
#
# l3 = list([1, '2', True])
# print(l3)

# a1 = array.array('i', [1, 2, 3])
# print(sys.getsizeof(a1))
# print(type(a1))

# 1. Какие еще типы кодов существуют?
#  'b': signed char, 'B': unsigned char, 'u': Unicode character
#  'h': signed short, 'H': unsigned short
#  'i': signed int, 'I': unsigned int
#  'l': signed long, 'L': unsigned long
#  'q': signed long long, 'Q': unsigned long long
#  'f': float, 'd': double

# 2. Напишите код, подобный приведенному выше, но с другим типом

a2 = array.array('f', [1.23, 2.34, 3.45])
print(sys.getsizeof(a2))
print(type(a2))

# a = np.array([1, 2, 3, 4, 5])
# print (type(a), a)
#
# # повышающее приведение типов
# a = np.array([1.23, 2, 3, 4, 5])
# print (type(a), a)
#
# a = np.array([1.23, 2, 3, 4, 5], dtype = int )
# print (type(a), a)
#
# a = np.array([range(i, i + 3) for i in [2, 4, 6]])
# print(a, type(a))

# a = np.zeros(10, dtype = int)
# print(a, type(a))
#
# print(np.ones((3, 5), dtype = float))
#
# print(np.full((4, 5), 3.1415))
#
# print(np.arange(0, 20, 2))
#
# print(np.eye(4))

# # 4. напишите код для создания массива с 5 равномерно распределенными случайными значениями, располагающимися
# # через равные интервалы в диапазоне от 0 до 1
print(np.linspace(0, 1, 5))
# # напишите код для создания массива с 5 нормально распределенными случайными значениями, располагающимися
# # с мат. ожиданием = 0 и дисперсией 1
print(np.random.normal(0, 1, 5))
#
# # напишите код для создания массива с 5 случайными целыми числами, располагающимися
# # в диапазоне [0, 10)
print(np.random.randint(0, 10, 5))

# Массивы

np.random.seed(1)

# x1 = np.random.randint(10, size = 3)
# x2 = np.random.randint(10, size = (3,2))
# x3 = np.random.randint(10, size = (3,2,2))
#
# print(x1)
# print(x2)
# print(x3)
# print(x1.ndim, x1.shape, x1.size)
# print(x2.ndim, x2.shape, x2.size)
# print(x3.ndim, x3.shape, x3.size)

#индекс (с 0)
# a = np.array([1, 2, 3, 4, 5])
# print(a[0])
#
# print(a[-2])
#
# a[1] = 20
# print(a)

# a = np.array([[1,2], [3,4]])
# print(a)
#
# print(a[0,0])
# print(a[-1,-1])
# a[1, 0] = 100
# print(a)

# a = np.array([1,2,3,4])
# b = np.array([1.0,2,3,4])
# print(a)
# print(b)
#
# a[0] = 10
# print(a)
#
# a[0] = 10.123
# print(a)

#срезы [start:finish:step] [0:shape:1]

# a = np.array([1,2,3,4,5,6])
# print(a[:3])
# print(a[3:])
# print(a[1:5])
# print(a[1:-1])
# print(a[1:6:2])
# print(a[1::2])
#
# print(a[::1])
# print(a[::-1])

# 7. Написать код для создания срезов массива 3 на 4
# - первые две строки и три столбца
# - первые три строки и второй столбец
# - все строки и столбцы в обратном порядке - второй столбец|
# - третья строка

a = np.array([[1,2,3],[4,5,6], [7,8,9], [10,11,12]])
print(a)
print(a[:2])
print(a[:3,1])
print(a[::-1])
print(a[2:0:-2])

# a = np.array([1,2,3,4,5,6])
# b = a[:3]
# b[0] = 100
# print(a)
# 8. Продемонстрируйте, как сделать срез-копию
a = [1, 2, 3, 4, 5]
print(a[:])
a = np.arange(1,13)
print(a)
print(a.reshape(2,6))
print(a.reshape(3,4))

# 9. Продемонстрируйте использование newaxis для получения вектора-столбца и вектора- строки
a = np.array([1,2,3,4,5])
print(a[np.newaxis,:]) #вектор-строка
print(a[:, np.newaxis]) #вектор-столбец

# x = np.array([1,2,3])
# y = np.array([4,5])
# z = np.array([6])
#
# print(np.concatenate([x,y,z]))

# x = np.array([1,2,3])
# y = np.array([4,5,6])
#
# r1 = np.vstack([x,y])
# print(r1)
# print(np.hstack([r1,r1]))
#10. Разберитесь, как работает метод dstack
a1 = np.array([[1, 2], [3, 4]])
a2 = np.array([[5, 6], [7, 8]])

print(np.dstack([a1,a2]))

# 11. Разберитесь, как работают методы split, vsplit, hsplit, dsplit
a1 = np.array([1, 2, 3, 4, 5, 6])
print(np.split(a1,3))

a2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(np.vsplit(a2,3))
print(np.hsplit(a2,2))

a3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
print(np.dsplit(a3,2))

### Вычисления с массивами
# Векторизированная операция - независимо к каждому элементу
# x = np.arange(10)
# print(x)
#
# print(x*2 + 1)
#
# # Универсальные функции
#
# print(np.add(np.multiply(x,2), 1))
# - - / // ** %

# 12. Привести пример использования всех универсальных функций

x = np.arange(10)
print(x)
print((x**2)/2 - 2)
print(np.subtract(np.divide(np.power(x, 2),2),2))

# x = np.arange(10)
# print(x)
# print(x%2)
# print(np.mod(x,2))
#
# x = np.arange(10)
# print(x)
# print(x//2)
# print(np.floor_divide(x,2))

##np.abs, sin/cos/tan, exp, log

# x = np.arange(5)
# y = np.zeros(10)
# print(np.multiply(x, 10, out=y[::2]))
# print(y)

# x = np.arange(1,5)
# print(x)
#
# print(np.add.reduce(x))
#
# print(np.add.accumulate(x))

# x = arange(1, 10)
# print(np.add.outer(x,x))
# print(np.multiply.outer(x,x))

