def list_item_generator(lst, iter_num=None):
    if iter_num is not None:
        count = 0
        while count < iter_num:
            for element in lst:
                yield element
            count += 1
    else:
        while True:
            for element in lst:
                yield element


lst = ['a', 'b']
for i in list_item_generator(lst, iter_num=2):
    print(i)
