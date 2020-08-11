def count(l):
    even = 0
    odd = 0
    for i in l:
        if i % 2 == 0:
            even = even +1

        else:
            odd = odd + 1
    return even,odd


lst = [66,11,25,33,2,1,3,7,10,30,50]

even,odd = count(lst)
print('even:{} and odd:{}'.format(even,odd ))
