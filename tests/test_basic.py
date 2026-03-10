# 知识点：assert 断言
# assert 表达式 → 为 True 就通过，为 False 就报错

def test_addition():
    """测试加法"""
    result = 1 + 1
    assert result == 2, "1+1应该等于2"

def test_string():
    """测试字符串操作"""
    url = "https://example.com/login"
    assert "login" in url, "URL应该包含login"
    assert url.startswith("https"), "URL应该以https开头"

def test_list():
    """测试列表操作"""
    test_data = ["admin", "user", "guest"]
    assert len(test_data) == 3, "列表应该有3个元素"
    assert "admin" in test_data, "列表应该包含admin"

def test_status_code():
    """模拟接口状态码验证"""
    expected_code = 200
    actual_code = 200  # 实际测试中这里是接口返回的值
    assert actual_code == expected_code, f"状态码错误：期望{expected_code}，实际{actual_code}"
# ====== 函数 ======
# 定义函数：def 函数名(参数):
def greet(name):
    """向用户打招呼"""
    print(f"你好，{name}！欢迎使用自动化测试框架")

# 调用函数
greet("香菜")


# 函数带返回值
def add(a, b):
    """计算两数之和"""
    return a + b

result = add(3, 5)
print(f"3 + 5 = {result}")


# 测试中最常见的函数用法：封装重复操作
def login(username, password):
    """模拟登录操作（后续会用 Selenium 真正实现这个）"""
    print(f"正在登录...")
    print(f"用户名：{username}")
    print(f"密码：{password}")
    return {"status": "success", "user": username}

response = login("admin", "123456")
print(f"登录结果：{response}")
