# tests/test_cases_with_fixture.py
import pytest
import requests

# 注意看！这里我们没有定义任何全局变量 GLOBAL_TOKEN
# 也没有在测试里写登录的代码

def test_get_legal_cases_with_fixture(login_token):
    """
    在括号里写上 `login_token`（就是 conftest.py 里那个函数名）。
    pytest 会自动先去执行 login_token 里的代码，
    然后把那个 yield 返回的真实 token 赋值给这里的 login_token 变量。
    """
    
    # 我们直接就能拿到 token 啦！
    print(f"用例开始执行，直接拿到了 Token: {login_token[:10]}...")
    
    url = "http://api.test.metalv.net/api/legal-cases?in_sign=LJ2641000047&limit=10&page=1&show_type=7"
    
    # 直接在 headers 里引用传进来的 login_token
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Authorization": f"Bearer {login_token}",
        "Referer": "http://39.96.211.164/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    res_data = response.json()
    
    assert res_data["code"] == 10000
    assert len(res_data["data"]["data"]) > 0
    assert res_data["data"]["data"][0]["in_sign"] == "LJ2641000047"
    
    print("✅ Fixture 版本案件查询测试通过！")
