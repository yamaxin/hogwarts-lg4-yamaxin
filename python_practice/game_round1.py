# 定义fight函数
def fight():
    # 定义用到的4个变量
    my_hp = 1000
    my_power = 200
    enemy_hp =1000
    enemy_power = 200

    # 定义最终血量计算
    my_final_hp = my_hp - enemy_power
    enemy_final_hp = enemy_hp - my_power

    # 判断输赢
    if my_final_hp > enemy_final_hp:
        print('我赢了')
    elif my_final_hp < enemy_final_hp:
        print('我输了')
    else:
        print('平局')

    # 三目运算，等同于if-else
    print('我赢了') if my_final_hp > enemy_final_hp else print('我输了')
fight()