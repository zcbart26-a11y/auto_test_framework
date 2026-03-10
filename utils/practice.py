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


# ====== 条件判断 ======
status_code = 200
if status_code == 200:
    print("✅ 请求成功")
elif status_code == 404:
    print("❌ 页面不存在")
elif status_code == 500:
    print("💥 服务器错误")
else:
    print(f"⚠️ 未知状态码：{status_code}")
# 测试中常用：判断登录结果
def check_login_result(response):
    """检查登录接口返回是否成功"""
    if response["status"] == "success":
        print(f"✅ 登录成功，欢迎 {response['user']}")
        return True
    else:
        print("❌ 登录失败")
        return False
# 用上面写好的 login() 函数测试
res = login("admin", "123456")
check_login_result(res)


# ====== 文件读写 ======
import json
def load_test_users(filepath):
    """从 JSON 文件读取测试用户数据"""
    with open(filepath, "r", encoding="utf-8") as f:
        users = json.load(f)
    return users
# 读取测试数据
users = load_test_users("../data/users.json")
print(f"\n共加载 {len(users)} 个测试用户：")
for user in users:
    print(f"  角色：{user['role']}，用户名：{user['username']}")