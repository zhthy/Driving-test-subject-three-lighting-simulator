import random
non = True
values = [1, 2, 3, 4, 5, 6,7,8,9,10,11,12,13]
while non:
    if random.choice(values) == 1:
        print("请开启前照灯")
        print("1近光灯")
        print("2远光灯")
        print("3远近光灯交替")
        print("4示阔灯和危险报警灯")
        a = float(input(""))
        if a == 1:
            print("yes")
        else:
            non = False
            print("no")
    if random.choice(values) == 2:
        print("夜间通过有信号灯控制的路口")
        print("1近光灯")
        print("2远光灯")
        print("3远近光灯交替")
        print("4示阔灯和危险报警灯")
        a = float(input(""))
        if a == 1:
            print("yes")
        else:
            print("no")
            non = False
    if random.choice(values) == 3:
        print("夜间与机动车会车")
        print("1近光灯")
        print("2远光灯")
        print("3远近光灯交替")
        print("4示阔灯和危险报警灯")
        a = float(input(""))
        if a == 1:
            print("yes")
        else:
            print("no")
            non = False
    if random.choice(values) == 4:
        print("夜间同方向近距离跟车")
        print("1近光灯")
        print("2远光灯")
        print("3远近光灯交替")
        print("4示阔灯和危险报警灯")
        a = float(input(""))
        if a == 1:
            print("yes")
        else:
            print("no")
            non = False
    if random.choice(values) == 5:
        print("夜间在有路灯照明良好的道路上行驶")
        print("1近光灯")
        print("2远光灯")
        print("3远近光灯交替")
        print("4示阔灯和危险报警灯")
        a = float(input(""))
        if a == 1:
            print("yes")
        else:
            print("no")
            non = False
    if random.choice(values) == 6:
        print("夜间在窄桥与非机动车会车")
        print("1近光灯")
        print("2远光灯")
        print("3远近光灯交替")
        print("4示阔灯和危险报警灯")
        a = float(input(""))
        if a == 1:
            print("yes")
        else:
            print("no")
            non = False
    if random.choice(values) == 7:
        print("夜间进入照明不良的道路行驶")
        print("1近光灯")
        print("2远光灯")
        print("3远近光灯交替")
        print("4示阔灯和危险报警灯")
        a = float(input(""))
        if a == 2:
            print("yes")
        else:
            print("no")
            non = False
    if random.choice(values) == 8:
        print("夜间进入无照明的道路行驶")
        print("1近光灯")
        print("2远光灯")
        print("3远近光灯交替")
        print("4示阔灯和危险报警灯")
        a = float(input(""))
        if a == 2:
            print("yes")
        else:
            print("no")
            non = False
    if random.choice(values) == 9:
        print("夜间通过拱桥")
        print("1近光灯")
        print("2远光灯")
        print("3远近光灯交替")
        print("4示阔灯和危险报警灯")
        a = float(input(""))
        if a == 3:
            print("yes")
        else:
            print("no")
            non = False
    if random.choice(values) == 10:
        print("夜间通过坡路")
        print("1近光灯")
        print("2远光灯")
        print("3远近光灯交替")
        print("4示阔灯和危险报警灯")
        a = float(input(""))
        if a == 3:
            print("yes")
        else:
            print("no")
            non = False
    if random.choice(values) == 11:
        print("超车")
        print("1近光灯")
        print("2远光灯")
        print("3远近光灯交替")
        print("4示阔灯和危险报警灯")
        a = float(input(""))
        if a == 3:
            print("yes")
        else:
            print("no")
            non = False
    if random.choice(values) == 12:
        print("夜间通过没有交通信号灯控制的路口")
        print("1近光灯")
        print("2远光灯")
        print("3远近光灯交替")
        print("4示阔灯和危险报警灯")
        a = float(input(""))
        if a == 3:
            print("yes")
        else:
            print("no")
            non = False
    if random.choice(values) == 13:
        print("路边临时停车")
        print("1近光灯")
        print("2远光灯")
        print("3远近光灯交替")
        print("4示阔灯和危险报警灯")
        a = float(input(""))
        if a == 4:
            print("yes")
        else:
            print("no")
            non = False
