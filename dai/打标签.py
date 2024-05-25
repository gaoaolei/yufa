# -*- encoding=utf8 -*-
__author__ = "lenovo"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


i = 0
index = 8
while True:
    if i > 199:
        index = index + 1
        i = 0
    poco(name='com.tencent.mm:id/odf')[-1].click()  # 点击页面中最后一个人
    if not poco(text='设置备注和标签').exists():
        keyevent("BACK")
        sleep(0.2)
        swipe((500, 997), (500, 800))
        continue
    poco(text='设置备注和标签').click()
    poco(text='添加标签').click()
    poco(text='群发%s' % index).click()
    poco(text='保存').click()
    poco(text='完成').click()
    sleep(0.2)
    keyevent("BACK")
    sleep(0.2)
    swipe((500, 997), (500, 800))
    i += 1
    print(i)


