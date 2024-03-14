# Python的多线程可以通过threading模块来实现:

# import threading
# thread_obj = threading.Thread([group [, target [, name [, args [, kwargs]]]]])
# group:暂时无用，未来功能的预留参数
# target:执行的目标任务名
# args:以元组的方式给执行任务传参
# kwargs:以字典方式给执行任务传参
# name:线程名，一般不用设置

# #启动线程，让线程开始工作
# thread obj.start()
import time
import threading


def sing():
    while 1:
        print("我在唱歌，啦啦啦啦啦")
        time.sleep(1)

def say(msg):
    while 1:
        print(msg)
        time.sleep(1)


if __name__ == '__main__':
    # 创建线程对象
    say_thread1 = threading.Thread(target=say, args=("你好",))
    sing_thread = threading.Thread(target=sing)
    say_thread2 = threading.Thread(target=say, kwargs={"msg": "再见"})
    # 启动线程
    say_thread1.start()
    sing_thread.start()
    say_thread2.start()
