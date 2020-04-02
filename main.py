import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox

def calculate(num1, num2):
    res = int(num1, 2)+int(num2, 2)
    temp = int('10000000000000000', 2)
    if res >= temp:
        res = res - temp + 1
    return format(res, '#018b')


def flip(num):
    return bin(((1 << 16) + (~int(num, 2))))


num1 = input('请输入第一个数字')
num2 = input('请输入第二个数字')
num3 = input('请输入第三个数字')
textbox1 = TextBox(plt.axes([0.25, 0.35, 0.6, 0.1]), "result is",
                   initial=flip(calculate(calculate(num1, num2), num3)))
plt.show()
