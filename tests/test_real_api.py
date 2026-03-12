# tests/test_real_api.py
import pytest
import requests

def test_real_login():
    """测试真实的登录接口"""
    # 1. 准备请求数据
    url = "http://api.test.metalv.net/api/login"
    payload = {
        "username": "15511111111",
        "password": "aa123456"
    }

    print("\n--- 正在请求真实登录接口 ---")
    
    # 2. 发送 POST 请求（通常登录接口是用 POST，如果不行等下我们换 GET）
    # json=payload 会自动帮我们把字典转成 JSON 格式发送
    response = requests.post(url, json=payload)
    
    # 获取接口返回的完整数据
    res_data = response.json()
    
    # 3. 打印出接口返回的真实信息，方便调试看结果
    print(f"HTTP 状态码: {response.status_code}")
    print(f"接口返回结果: {res_data}")
    
    # 4. 断言（校验接口是否真的成功了）
    # 第一层校验：HTTP 状态码必须是 200（代表网络请求成功到达了服务器）
    assert response.status_code == 200
    
    # === 业务断言 ===
    # 你的接口成功时返回：{'code': 10000, 'message': '登录成功', 'data': {'token': '...'}}
    
    # 校验1：判断 code 必须等于 10000
    assert res_data["code"] == 10000, f"期望 code 是 10000，实际却是 {res_data['code']}"
    
    # 校验2：判断 message 必须等于 '登录成功'
    assert res_data["message"] == "登录成功"
    
    # 校验3（进阶）：判断成功后，一定要有 token 返回
    # token 在 data 字典里面，所以要用 res_data["data"]["token"] 获取
    token = res_data["data"]["token"]
    assert token != "", "登录成功了，但是似乎没有返回 token"
    
    print("\n✅ 测试通过！成功获取到了 Token:", token)
