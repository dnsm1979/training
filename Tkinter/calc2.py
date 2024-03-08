import operator as op

def func(oper):
    funcs_names = {
        '+':  op.__add__,
        '*':  op.__mul__ ,
        '-':  op.__sub__,
        '/':  op.truediv
    }
    try:
        return funcs_names[oper]
    except KeyError:
        raise ValueError('Неверная операция')


print(func('*')(5, 7))  # 35