# tests/ui/test_login_pom.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
import time

def test_login_success():
    """
    用 POM 模式重构的测试用例
    这里只有“测试逻辑”和“断言”，完全看不到复杂的元素定位(find_element)
    """
    print("\n[POM 模式测试] 启动浏览器(无头模式)...")
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)
    
    try:
        # 1. 实例化我们的 Page Object (页面对象)
        login_page = LoginPage(driver)
        
        # 2. 执行业务操作：打开页面 -> 登录
        print("[POM 模式测试] 调用 LoginPage.open()...")
        login_page.open()
        
        print(f"[POM 模式测试] 调用 LoginPage.login(standard_user)...")
        login_page.login("standard_user", "secret_sauce")
        
        # 3. 断言环节
        # 登录成功后会进入商品页，商品页的标题 class="title"，里面写着 Products
        # 为了演示，我们暂时直接查这个标题（之后如果有复杂的页面可以再写个 ProductsPage）
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        
        header_text = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "title"))
        ).text
        
        assert header_text == "Products", f"期望标题是 Products，实际是 {header_text}"
        print("✅ POM 模式重构版本的 UI 测试完美通过！")
        
    finally:
        driver.quit()
