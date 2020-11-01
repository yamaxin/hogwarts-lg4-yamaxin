class Game:
    # 定义fight函数
    def __init__(self, my_hp ,enemy_hp):
        # 定义用到的4个变量
        self.my_hp = my_hp
        self.my_power = 200
        self.enemy_hp = enemy_hp
        self.enemy_power = 200

    def fight(self):
        # 加入循环，让游戏进行多轮
        while True:
            self.my_hp = self.my_hp - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power
            print(self.my_hp)
            # 判断谁的血量小于等于0
            if self.my_hp <= 0:
                print('我输了')
                # 满足条件跳出循环
                break
            elif self.enemy_hp <= 0:
                print('我赢了')
                break
    # 定义休息方法
    def rest(self, time_num):
        print(f'太累了，休息{time_num}分钟')




class HouYi(Game):
    def __init__(self, my_hp ,enemy_hp):
        # 定义护甲属性
        self.defense = 100
        # 通过继承调用父类构造函数，调用父类属性
        super().__init__(my_hp ,enemy_hp)

    #改造fight方法
    def final(self):
        # 加入循环，让游戏进行多轮
        while True:
            # 修改my_hp计算方式
            self.my_hp = self.my_hp + self.defense - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power
            print(self.my_hp)
            # 判断谁的血量小小于等于0
            if self.my_hp <= 0:
                print('我输了')
                # 满足条件跳出循环
                break
            elif self.enemy_hp <= 0:
                print('我赢了')
                break




houyi = HouYi(2000,1000)
houyi.fight()
houyi.rest(3)