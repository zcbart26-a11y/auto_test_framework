# pages/login_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    """
    登录页面模型 (Page Object)
    这里只放和“登录页面”相关的数据（元素怎么定位）和操作（怎么登录）
    不放任何测试断言 (assert)
    """
    
    # 1. 把页面上所有要用到的元素定位，统一定义在这里（也就是“数据分离”）
    # 如果有一天前端把 id 改了，只用在这里改一行就行，测试用例不用动！
    URL = "https://www.saucedemo.com/"
    LOC_USERNAME = (By.ID, "user-name")
    LOC_PASSWORD = (By.ID, "password")
    LOC_LOGIN_BTN = (By.ID, "login-button")
    
    # 2. 封装页面专属操作：打开本页
    def open(self):
        self.open_url(self.URL)
        
    # 3. 封装页面关键业务操作：执行登录
    def login(self, username, password):
        # 复用父类 BasePage 里的通用方法
        self.input_text(self.LOC_USERNAME, username)
        self.input_text(self.LOC_PASSWORD, password)
        self.click_element(self.LOC_LOGIN_BTN)
