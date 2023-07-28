import random

door_num = 3
car = 0;sheep = 0

xhcs = 1000
for k in range(0,xhcs):
    car_in_num = random.randint(0, door_num-1)
    print("本次 车在 %d 号门" %car_in_num)
    # 某门后有车 1 为 车
    door = [0] * door_num
    door[car_in_num] = 1

    # 随机选取一扇门
    choice = random.randint(0, door_num-1)
    print("本次 玩家选择 %d 号门" %choice)
    # 主持人在 未选择的两扇门中打开一扇有 羊的门
    index = []
    c = -1
    for i in door:
        c += 1
        if c == choice:
            continue
        elif door[c] == 1:
            continue
        else:
            index.append(c)
    if len(index) == 1:
        host_open = index[0]
    else:
        host_open = index[random.randint(0, len(index)-1)]
    print("本次 主持人打开 %d 号门" %host_open)
    # 计算剩余 1 扇门有车的概率
    for i in range(0,door_num):
        if i != choice and i != host_open:
            ret = door[i]
    if ret == 1:
        car += 1
        print('玩家换门后获得汽车!')
    else:
        sheep += 1
        print('玩家换门后没有获得汽车!')
    print('-' *50)

print("经过 %d 次实验" %xhcs)
print("换门后 获得奖品的次数为 %d" %car)
print("不换门 获得奖品的次数为 %d" %sheep)