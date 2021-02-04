# -*- encoding=utf8 -*-
__author__ = "liuyayun"

from airtest.core.api import *

auto_setup(__file__)


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
poco(text="账户").click()
poco(text="精选").click()
poco(text="Comic").click()
poco(text="Novel").click()
poco(text="书架").click()
poco(text="书库").click()
