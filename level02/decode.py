def decoder():
    str = '0x756e5052343768480x45414a35617339510x377a7143574e67580x354a35686e4758730x48336750664b394d'
    lst = str.split('0x')[1:]

    index = (14, 12, 10, 8, 6, 4, 2, 0)
    for i in lst:
        for j in index:
            print(f'{i[j]}{i[j+1]}', end='')


decoder()