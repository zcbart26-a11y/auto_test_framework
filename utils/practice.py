# 变量
name = "香菜"
age = 25
is_tester = True

# 字符串拼接
print("我的名字是：" + name)
print(f"我今年 {age} 岁")  # f-string，推荐写法
print(f"我是测试工程师：{is_tester}")

# 测试中常用：获取URL、账号密码
base_url = "https://example.com"
username = "admin"
password = "123456"
print(f"登录地址：{base_url}/login")

# 列表 - 存多个数据（测试中常用来存测试用例数据）
test_urls = ["/login", "/home", "/profile", "/logout"]
print(f"共有 {len(test_urls)} 个页面需要测试")
print(f"第一个页面：{test_urls[0]}")  # 下标从0开始

# 遍历列表
for url in test_urls:
    print(f"测试页面：{base_url + url}")

# 字典 - 存键值对（测试中常用来存请求参数）
login_data = {
    "username": "admin",
    "password": "123456",
    "remember_me": True
}
print(f"\n登录用户名：{login_data['username']}")
print(f"登录密码：{login_data['password']}")

# 异常处理 - 防止程序崩溃
def read_config(filename):
    """读取配置文件"""
    try:
        with open(filename, "r") as f:
            content = f.read()
            print(f"配置文件内容：{content}")
    except FileNotFoundError:
        print(f"❌ 文件不存在：{filename}")
    except Exception as e:
        print(f"❌ 发生未知错误：{e}")
    finally:
        print("读取操作结束")  # 无论成功失败都会执行

# 测试：读取不存在的文件
read_config("config/settings.ini")
