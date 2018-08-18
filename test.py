import pickle
chatname = str(format('2000000007')) + '.pkl'
try:
    input = open(chatname, 'rb')
    sss = True
except FileNotFoundError:
    text = 'Сначала нужно зарегистрироваться и провести один розыгрыш! Для помощи напиши пидорпомощь.'
    sss = False
if sss:
    obj = pickle.load(input)
    print(obj)
    print('--------------')
    input.close()
    ob = list(obj.values())
    ob = ob[1:]
    ob.sort(key=lambda s: s[1], reverse=True)
    top = 'Топ-10 пидоров за все время:'
    if len(ob) < 10:
        f = len(ob)
    else:
        f = 10
    for i in range(1, f + 1):
        top += '\n' + str(i) + '. ' + ob[-1 + i][0] + ' — ' + str(ob[-1 + i][1]) + ' раз(а)'
    print(top)


