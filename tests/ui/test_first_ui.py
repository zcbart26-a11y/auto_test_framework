# tests/ui/test_first_ui.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_saucedemo_login():
    """我们的第一个 UI 自动化脚本：打开一个电商沙盒网站并自动登录"""
    print("\n[UI 自动化] 准备启动浏览器...")
    
    # 初始化 Chrome 浏览器实例 (这会自动弹出一个真实的谷歌浏览器)
    driver = webdriver.Chrome()
    
    try:
        # 为了能看清楚它的自动操作，我们让它动作慢一点
        driver.implicitly_wait(10) # 隐式等待最多10秒
        
        # 1. 访问专门用于测试的沙盒网站 (Sauce Demo)
        print("[UI 自动化] 正在打开测试沙盒网站 Sauce Demo...")
        driver.get("https://www.saucedemo.com/")
        time.sleep(1) # 停顿1秒让你看清画面
        
        # 2. 元素定位与操作：找到用户名输入框，输入账号
        print("[UI 自动化] 定位用户名输入框，输入 'standard_user'...")
        username_input = driver.find_element(By.ID, "user-name")
        username_input.send_keys("standard_user")
        time.sleep(1)
        
        # 3. 元素定位与操作：找到密码输入框，输入密码
        print("[UI 自动化] 定位密码输入框，输入 'secret_sauce'...")
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("secret_sauce")
        time.sleep(1)
        
        # 4. 找到登录按钮并点击
        print("[UI 自动化] 点击登录按钮...")
        login_btn = driver.find_element(By.ID, "login-button")
        login_btn.click()
        time.sleep(2) # 停顿2秒看登录后的商品列表页
        
        # 5. 非常重要！UI自动化也需要断言，否则怎么知道登录成功了？
        # 我们寻找登录后才有的商品列表标题栏 (class="title")
        header_title = driver.find_element(By.CLASS_NAME, "title").text
        print(f"[UI 自动化] 登录后的页面标题是: '{header_title}'")
        assert header_title == "Products"
        
        print("\n✅ 第一个 UI 自动化脚本完美执行成功！登录流程测试通过！")
        
    finally:
        # 测试结束后关闭浏览器
        print("[UI 自动化] 正在关闭浏览器释放资源...")
        driver.quit()
