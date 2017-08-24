# -*- coding: utf-8 -*-

l = [1, 2, 3, 4, 5]

print(l[1], l[2], l[4], l[-3])

l.append(6)

print(l)

l.insert(1, 8)

print(l)

l.pop()

print(l)

l.pop(1)

print(l)

l.insert(1, [11, 12])

Len = []

print(l, len(l), len(Len))

tuple = (1, 29, 0, 8)

# tuple[0] = 10     # 错误  'tuple' object does not support item assignment

# 元组不可变，也没有append，insert这些方法

t = (1, 2, 3, [5, 6], 10)

t[3][1] = 4

print(t)

t = (1, 2, (9, 0))

# t[2][0] = 0  # 错误  'tuple' object does not support item assignment

print(t)

x = list(range(2, 10))

print(x)

y = ['Hello', 'World', 'IBM', 'Apple']

h = [w.lower() for w in y]  # 列表生成式，注意外边的括号

print(h)
