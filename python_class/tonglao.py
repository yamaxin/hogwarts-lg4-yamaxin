'''定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“师弟是我的！”，如果传入“丁春秋”，打印“叛徒！我杀了你”
fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造
'''

class TongLao:
    def __init__(self, my_hp, my_power, enemy_hp, enemy_power):
        # 定义自己的武力值
        self.my_hp = my_hp
        self.my_power = my_power
        # 定义敌人的血量和武力值
        self.enemy_hp = enemy_hp
        self.enemy_power = enemy_power


    # 定义see_people方法
    def see_people(self, name):
        # 定义name参数
        self.name = name

        # 根据传入的name，进行分支判断
        if self.name == 'WYZ':
            print('师弟！！！！')
        elif self.name == '李秋水':
            print('师弟是我的!')
        elif self.name == '丁春秋':
            print('叛徒！我杀了你')

    # 定义fight_zms方法
    def fight_zms(self):
        # 重新计算自己的血量和武力值
        self.my_new_hp = self.my_hp/2
        self.my_new_power = self.my_power*10

        # 计算剩余的武力值
        self.my_hp1 = self.my_new_hp - self.enemy_power
        self.enemy_hp1 = self.enemy_hp - self.my_new_power

        # 判断谁的血量小于等于0
        if self.my_hp1 <= 0:
            print('我输了')
            # 满足条件跳出循环
        elif self.enemy_hp1 <= 0:
            print('我赢了')



tonglao=TongLao(1000,1000,200,100)
tonglao.fight_zms()



