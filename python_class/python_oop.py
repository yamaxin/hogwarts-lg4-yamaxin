# 面向对象
class House:
    # 静态属性->类变量（类之中，方法之外）
    door = 'red'
    floor = 'white'

    # 构造函数，类实例化时直接执行(实例化变量最好放在构造函数中)
    def __init__(self):
        # 在方法当中调用类变量需要加self，self表示类对象本身
        print(self.door)
        # 在实例变量中，类当中，方法房子，以'self.变量名'去定义
        self.kitchen = 'cook'

    # 动态方法
    def sleep(self):
        # 定义普通变量（类当中，方法当中，前面没有self）
        bed = '席梦思'
        # 在普通方法中定义实例变量
        self.table = '桌子上可以放东西'
        print(f'在房子里可以躺在{bed}上睡觉')

    def cook(self):
        print('在房子里可以做饭')
        print(self.kitchen)
        print(self.table)

# 把类实例化
# 北欧风格房子
North_house = House()
North_house.sleep()
North_house.cook()
#中式房子
#China_house = House()

# #调用类属性
# print(House.door)
# # 实例对象调用类属性
# print(North_house.door)

# 修改类属性
# House.door = 'yellow'
# print(House.door)

# 通过实例对象修改类属性
# North_house.door = 'black'
# print(North_house.door)
# print(House.door)
# print(China_house.door)


