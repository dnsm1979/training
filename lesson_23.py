# import threading
# try:
#     arcs = input('Числа через пробел: ').split()
#     user_int_input = (int(x) for x in arcs)
# except TypeError:
#     print('Incorrect input!')
#
#
# def sum_arcs(arc):
#
#     print(sum(arc))
#
# def arith_arcs(arc):
#     print(sum(arc) / len(arc))
#
#
#
# if __name__ == '__main__':
#     sum_threading = threading.Thread(target=sum_arcs, args=(user_int_input,))
#     arith_threading = threading.Thread(target=arith_arcs, args=(user_int_input,))
#
#     sum_threading.start()
#     arith_threading.start()
#
#     sum_threading.join()
#     sum_threading.join()
#
