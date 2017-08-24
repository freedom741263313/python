class practise(object):
    """docstring for practise"""

    def __init__(self, arg):
        super(practise, self).__init__()
        self.arg = arg

    def hello(self):
        print('a')

    # def hello():
    #     print('a')    #  takes 0 positional arguments but 1 was given

    # 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称，但是在调用这个方法的时候你不为这个参数赋值，Python会提供这个值。这个特别的变量指对象本身，按照惯例它的名称是self


if __name__ == '__main__':
    p = practise('a')
    p.hello()
