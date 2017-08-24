# 输入、输出
print('I', 'am', 'a Chinese man!')  # 逗号会显示为空格

# name = input('Please enter your name:')
# print('Your name:', name)

print(r'\\\t\\')  # r''表示''内部的字符串默认不转义

print('''line1
 line2
 line3''')       # '''...'''的格式表示多行内容，还可以在前面加上r使用

print(10 / 3)

print(10 // 3)   # 表示地板除

print(1024 * 768)

print(ord('中'), ord('a'))  # ord获取字符的整数显示

print(chr(25991))  # chr编码显示为中文

print('\u4e2d\u6587')  # 16进制显示字符

print(b'ABC')  # b前缀表示字节类型

print('中文'.encode('utf-8'))  # encode编码为制定的bytes

print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))  # decode解码字节为字符

# 1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节

print(len('ABC'), len('中文'), len(b'ABC'), len(
    b'\xe4\xb8\xad\xe6\x96\x87'), len('中文'.encode('utf-8')))

print('hello,%s' % 'world')  # 格式化

print('Hello,%s %s' % ('dear', 'Mom'))

print('%.2f' % 3.1415)

print('hello %s %%' % 'world')  # 字符串%是一个普通字符
