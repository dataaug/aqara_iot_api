# 鼠标键盘监控
from pynput import keyboard, mouse
# 日志处理
# from loguru import logger
from request_aqara import wink, light_adjust
# 多线程处理
from threading import Thread
import time

class light_your_tap():
    def __init__(self):
        self.record = []

        # 开启灯泡

    def on_keyboard_press(self, key):
        '''
        按键时记录所按下的键
        :param key:
        :return:
        '''
        print(f'{key} :被按下了')
        # wink()
        # logger.debug(f'{key} :被按下了')
        # if key >= 'a' and key <= 'z': # 只有A到Z之间输入影响灯泡
        self.record.append([key, time.time()])
        # self.adjust_action()
        # print('len(record):', len(self.record))
        # # if key
        # if key >= 'a' and key <= 'z' : #  只有A到Z之间输入影响灯泡
        # self.record.append([key, time.time()])
        # print('len(record)')
        

    def on_keyboard_release(self, key):
        '''
        释放按键处理函数
        :param key:
        :return:
        '''
        if key == keyboard.Key.esc:
            return False
    
    def adjust_action(self):
        time_thred = time.time() - 3
        self.record = [x for x in self.record if x[1] > time_thred]

        # 2700-6500K
        
        strength = len(self.record)
        # if strength >= 1:
        # if strength >= 1:
            #2700 + (strength - 1) * 100
            #ajust_light(int(1000000 / ))
        light_adjust(min(100, strength * 4), min(6500,2700 + strength * 100) )

    def update_queue(self): # 每秒钟检测数组情况
        while True:
            self.adjust_action()
            time.sleep(1)

    def func_keyboard(self):
        '''
        键盘的按下/释放的监听
        :return:
        '''
        with keyboard.Listener(on_press=self.on_keyboard_press, on_release=self.on_keyboard_release) as keyboard_listener:
            keyboard_listener.join()

if __name__ == '__main__':
    '''
    执行线程
    '''
    tool = light_your_tap()
    thread_keyboard = Thread(target = tool.func_keyboard)
    thread_light_change = Thread(target = tool.update_queue)

    # # 分别启动线程
    thread_keyboard.start()
    thread_light_change.start()

    # 定义键盘监听线程
    # thread_keyboard = Thread(target=func_keyboard)
    # # 定义鼠标监听线程
    # thread_mouse = Thread(target=func_mouse_click)
    # # 分别启动线程
    # thread_keyboard.start()
    # thread_mouse.start()