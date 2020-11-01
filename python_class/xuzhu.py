from python_class.tonglao import TongLao

class Xuzhu(TongLao):
    # 定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
    def read(self):
        # 打印罪过罪过
        print('罪过罪过')

xuzhu = Xuzhu(1000,2000,100,200)
xuzhu.read()
