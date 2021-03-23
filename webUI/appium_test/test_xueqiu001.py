

from appium import webdriver

desire_cap = {
  "platformName": "Android",
  "deviceName": "127.0.0.1:7555",
  "appPackage": "com.xueqiu.android",
  "appActivity": "com.xueqiu.android.common.MainActivity",
  "noReset": True,                    # 不重置
  "dontStopAppOnReset": True,         # 执行结束后不停止app，可继续使用
  "skipDeviceInitialization": True    # 跳过安装和权限设置
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
driver.implicitly_wait(5)

els1 = driver.find_elements_by_id("\tcom.xueqiu.android:id/title_text")
els2 = driver.find_elements_by_id("com.xueqiu.android:id/title_text")
el1 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el2.send_keys("长城汽车")
el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]")
el3.click()
driver.quit()