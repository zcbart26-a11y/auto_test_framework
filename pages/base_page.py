# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """
    所有页面的基类
    封装了最常用的底层操作，比如打开网页、找元素、输入、点击。
    这样别的页面就不需要每次都写长长的 WebDriverWait 和 find_element 了。
    """
    
    def __init__(self, driver):
        self.driver = driver
        # 默认显式等待时间为 10 秒
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=0.5)

    def open_url(self, url):
        """打开对应的网址"""
        self.driver.get(url)

    def find_element(self, locator):
        """
        寻找元素并加入了显式等待
        locator 是一个元组，例如: (By.ID, 'user-name')
        """
        # 直到元素可见才返回，比 implicitly_wait 更稳健
        return self.wait.until(EC.visibility_of_element_located(locator))

    def input_text(self, locator, text):
        """找到输入框，清空后输入文字"""
        ele = self.find_element(locator)
        ele.clear()
        ele.send_keys(text)

    def click_element(self, locator):
        """找到元素并点击"""
        # 一般点击需要等到元素可被点击
        ele = self.wait.until(EC.element_to_be_clickable(locator))
        ele.click()
        
    def get_element_text(self, locator):
        """获取元素的文本内容"""
        return self.find_element(locator).text
