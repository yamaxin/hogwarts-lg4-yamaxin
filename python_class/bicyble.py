# 自行车类
class Bicyble:
    def run(self, km):
        print(f'一共用脚骑了{km}公里，累死了')

# 电动自行车
class Ebicyble(Bicyble):
    # 定义电量，属性需要传参定义，可以直接放到构造函数中
    def __init__(self,valume):
        self.valume = valume

    # 充电方法
    def fill_charge(self, vol):
        # 充电后的电量 = 本身的电量+充电电量
        self.valume = self.valume + vol
        print(f'充了{vol}度电，现在电量是{self.valume}度')


    # 骑行方法
    def run(self,km):
        # 1、获取目前电量所能电动骑行的最大里程数
        power_km = self.valume*10
        if power_km >= km:
            print(f'使用电瓶电量骑行了{km}km')
        else:
            # 电量不够了，在电用完后，用脚骑行
            print(f'使用电瓶电量骑行了{power_km}km')
            #电量耗尽调用Bicyble的run方法
            # bike = Bicyble()
            # bike.run(km-power_km)

            # 继承调用
            super().run(km-power_km)


# bike = Bicyble()
# bike.run(10)
ebike = Ebicyble(10)
ebike.run(150)