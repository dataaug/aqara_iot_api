# aqara IOT API
### apara 官方开放API接口，注册后可获取token，通过指令控制家庭aqara设备。
### 通过api控制可以实现更多可能
### 在注册apara开发者平台个人开发者过后，填写params.py中对应的Accesstoken，Appid，Keyid，AppKey,就可以调用requst_aqara中的request方法，指定[官网开放API接口](https://opendoc.aqara.cn/docs/云对接开发手册/API文档.html)中的任意类型进行家庭aqara设备api控制

### 使用教程: [个人开发者申请以及代码使用视频](https://www.bilibili.com/video/BV1Ut4y1V72A?spm_id_from=333.1007.top_right_bar_window_history.content.click&vd_source=b8dab1f72c8ae5a45bf94e47e415e82d)


## 8月15日更新
新增“内卷传感器”，根据键盘输入频率改变灯的色温和亮度
新增依赖 pip3 install pynput (用于监测键盘输入)
按照上述的教程填入params中的参数，以及在官网找到自己灯泡的subjectId，替换commands.py中对应字段
然后python3 listen.py 即可启动“内卷传感器”






































