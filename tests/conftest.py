# tests/conftest.py
import pytest
import requests

# 这个文件是 pytest 的“魔法文件”
# 只要把它放在 tests/ 目录下，里面定义的所有 fixture 都不需要导入，
# 所有测试文件都能直接用！

@pytest.fixture(scope="session")
def login_token():
    """
    公共前置操作：登录并获取 Token。
    scope="session" 意味着在整个测试执行过程中，这层代码只会跑一次，
    拿到 Token 后就一直复用，极大提升测试速度！
    """
    print("\n[Fixture] 正在执行全局登录，获取 Token...")
    url = "http://api.test.metalv.net/api/login"
    payload = {
        "username": "15511111111",
        "password": "aa123456"
    }
    
    response = requests.post(url, json=payload)
    res_data = response.json()
    token = res_data["data"]["token"]
    
    print(f"[Fixture] 成功拿到全局 Token: {token[:15]}...\n")
    
    # yield 后面的值，就是传给测试用例的返回值
    yield token
    
    # 理论上可以在这后面写退出登录的清理逻辑（后置操作）
    # print("\n[Fixture] 测试结束，执行清理操作（如有）")
